import numpy as np
import prince
import matplotlib.pyplot as plt

## plot cumulative variance for PCA analysis
def plot_cumulative_variance_pca(X:np.array, ax:"axes", variance_threshold:float = .95, is_mixed:bool = False)->"axes":
    """
    Plot cumulative variance for PCA analysis.
    X -- df or numpy array with data analyzed by PCA.
    ax -- Matplotlib axes to be used to plot the current chart.
    variance_threshold -- Value of cumulative variance to be used as limit (default, 0.95).
    is_mixed -- If variables to be analized are mixed num/cat or only numerical (default, False).
    return -- Matplotlib axes with the current chart added.
    """
    # x values
    xi = np.arange(1, X.shape[1]+1, step=1)
    # estimate explained variance for the maximun number of components
    if is_mixed:
        explained_variance = prince.FAMD(n_components=X.shape[1]).fit(X).explained_inertia_
    else:
        explained_variance = prince.PCA(n_components=X.shape[1]).fit(X).explained_inertia_
    # estimate acumulative variance
    y = np.cumsum(explained_variance)
    # set limits in values
    plt.xlim(.9,X.shape[1]+.1)
    plt.ylim(0.0,1.1)
    # plot line
    plt.plot(xi, y, linestyle='--', color='b', alpha = .5)
    # plot dots
    plt.scatter(xi, y, color = 'b', alpha = 1., edgecolor = "black")
    # set labels and xticks
    plt.xlabel('Number of Components')
    plt.xticks(np.arange(1, X.shape[1]+1, step=1)) #change from 0-based array index to 1-based human-readable label
    plt.ylabel('Cumulative variance (%)')
    # set title
    plt.title('The number of components needed to explain variance')
    # horizontal line for threshold
    plt.axhline(y=variance_threshold, color='r', linestyle='-', alpha = .5)
    # draw theshold value
    plt.text(1., variance_threshold + .01, f'{variance_threshold * 100.}% cut-off threshold', color = 'red', fontsize=12)
    # set grid
    ax.grid(axis='x')
    # return axes
    return ax


## Automated selection of number of PCs for PCA. Mixed num/cat variables is possible.
def pca_number_pcs_auto_selection(X:np.array, 
                                  variance_threshold:float = .95, 
                                  is_mixed:bool = False, 
                                  is_rescale:bool = True, 
                                  verbose:bool = False)->int:
    """
    Automated selection of number of PCs for PCA. Mixed num/cat variables is possible.
    X -- df or numpy array to be analized.
    variance_threshold -- percent of variance to be used as cut-off threshold.
    is_mixed -- If variables to be analized are mixed num/cat or only numerical (default, False).
    is_rescale -- If rescale before PCA for only numerical variables (default, True).    
    verbose -- display extra information (default, False).
    return -- optimed number of pcs.
    """
    # loop of possible components number
    for nc in np.arange(1, X.shape[1]+1, 1):
        # initialize pca
        if is_mixed:
            total_explained_inertia = np.sum(prince.FAMD(n_components=nc).fit(X).explained_inertia_) 
        else:
            total_explained_inertia = np.sum(prince.PCA(n_components=nc, rescale_with_mean=is_rescale, rescale_with_std=is_rescale).fit(X).explained_inertia_)
        # validate
        if total_explained_inertia >= variance_threshold:
            # display result
            if verbose:
                print(f"Optimal number of PCs for {variance_threshold*100.}% cut-off threshold = {nc}")
            # return value of components number
            return nc
    # return if it is not found nothing
    return np.nan


## PCA analysis for mexed numerical and categorical variables
def analysis_pca(X:np.array, 
                 y:np.array = None, 
                 n_components:int = 2, 
                 is_mixed:bool = False, 
                 is_rescale:bool = True, 
                 threshold_corr:float = .5, 
                 random_state:int = 42, 
                 verbose:bool = True)->"transformer":
    """
    PCA analysis for mixed numerical and categorical variables.
    X -- df or numpy to be analized.
    y -- df series or numpy array with labels to be used to PCs distribution chart.
    n_components -- Number of components to be used (default, 2).
    is_mixed -- If variables to be analized are mixed num/cat or only numerical (default, False).
    is_rescale -- If rescale before PCA for only numerical variables (default, True).
    threshold_corr -- When it is analized the correlation between variables and components, 
                      it is the limit to consider a variable as high correlated or not (default, 0.5).
    random_state -- Seed (default, 42).
    verbose -- Display extra information and charts (default, True).
    return -- Fitted PCA transformed.
    """

    # initialize PCA according to if variables are mixed or only numerical
    if is_mixed:
        pca = prince.FAMD(
            n_components=n_components,
            n_iter=3,
            copy=True,
            check_input=True,
            random_state=random_state,
            engine="sklearn"
        )
    else:
        pca = prince.PCA(
            n_components=n_components,
            n_iter=3,
            rescale_with_mean=is_rescale,
            rescale_with_std=is_rescale,
            copy=True,
            check_input=True,
            engine='auto',
            random_state=random_state
        )
    # fit transformer
    try:
        pca = pca.fit(X)
    except Exception as e:
        print("[error] There are a problem with any column type.")
        print(str(e))
        raise ValueError('This analysis will be stopped.')
    
    """ display pca analysis """

    # display
    print(f"Number of components selected = {n_components}")
    explained_intertia = pca.explained_inertia_
    total_inertia = np.sum(explained_intertia)
    unexplained_intertia = 1. - total_inertia
    print(f'How much each PC explains part of the underlying of the distribution: {explained_intertia} / Total = {total_inertia} / Unexplained inertia = {unexplained_intertia}')
    
    ## plot pca analysis
    if verbose:
        import matplotlib.pyplot as plt
        fig, (ax1, ax2) = plt.subplots(ncols = 2, figsize = (16,8))
        # plot components 2 first components
        ax1 = pca.plot_row_coordinates(
            X,
            ax=ax1,
            x_component=0,
            y_component=1,
            labels=None,
            color_labels= None if y is None else y,
            ellipse_outline=False,
            ellipse_fill=True,
            show_points=True
        )  
        ax2 = plot_cumulative_variance_pca(X, ax2, variance_threshold = .95, is_mixed = is_mixed)
        plt.show()

    
        """ display the most correlated features per component """

        # correlation between components and variables
        dfcorr = pca.column_correlations(X)        
        # display title
        print("MOST CORRELACTED VARIABLES PER COMPONENT:")
        # initialize
        l_vars_most_correlated = list()
        # get list of components
        l_components = dfcorr.columns.tolist()
        # loop of components
        for comp in l_components:
            # collect most correleted
            dfmostcorr = dfcorr[np.abs(dfcorr[comp]) >= threshold_corr][[comp]]
            # collect its variables
            l_vars_most_correlated += dfmostcorr.index.tolist()
            # display
            print(dfmostcorr.to_dict())
        # remove duplicated variables
        l_vars_most_correlated = list(set(l_vars_most_correlated))
        # display final list without duplicates
        print(f'Final list of variables most correlected with components: {l_vars_most_correlated}')

    # return 
    return pca