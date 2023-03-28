import numpy as np
import pandas as pd
import sklearn.metrics as sklearn_metrics
from sklearn.cluster import KMeans
from src.pca import pca_number_pcs_auto_selection, analysis_pca


## Wrapper function of Scikit-learn's calinski_harabasz_score
def calinski_harabasz_score(X:np.array, labels:list)->float:
  """
  Wrapper function of Scikit-learn's calinski_harabasz_score. 
  The only difference is it doesn't throw an error where there is only one label.
  X -- df or numpy array of features.
  labels -- List of labels estimated with cluster.
  return -- Calinski Harabasz score.
  """
  
  if len(set(labels)) == 1:
    return float("NaN")
  else:
    return sklearn_metrics.calinski_harabasz_score(X, labels)


## Gives the same result of Scikit-learn's Kmeans, but it doesn't throw an error when n_clusters = 1.
def kmeans_labels(X:np.array, n_clusters:int)->np.array:
    """
    Gives the same result of Scikit-learn's Kmeans, but it doesn't throw an error when n_clusters = 1.
    X -- df or numpy array of features.
    n_clusters -- Number of clusters to be used with K-Means.
    return -- Number of labels.    
    """
    if n_clusters == 1:
        return np.repeat(a=0, repeats=len(X))
    else:
        return KMeans(n_clusters=n_clusters).fit(X).labels_
    

## Estimate local maximums of metric values
def local_maximums_metric(possible_k:np.array, array_metrics:np.array)->np.array:
    """
    Estimate local maximums of metric values.
    possible_k -- Array of possible values for number of clusters.
    array_metrics -- Array of corresponding values of estimated metric for each k value.
    return -- Array of local maximums (candidates to be the final k value to be used in K-Means).
    """
    # inputs validation
    assert len(possible_k) == len(array_metrics)
    # build df
    dfs = pd.DataFrame({'num_clusters':possible_k,'metric':array_metrics}).set_index("num_clusters")
    # estimate slopes
    dfs['metric_slope'] = dfs.diff() >= 0
    # collect data
    slopes = dfs.metric_slope.values
    num_clusters = dfs.index.values
    # initialize output
    local_maximums = list()
    # loop of metric values
    for i in range(1, len(dfs), 1):
        # validate if is a local maximum
        if slopes[i-1] == True and  slopes[i] == False:
            # append result
            local_maximums.append(num_clusters[i-1])
    # return results
    return np.array(local_maximums)
    

## Estimate candidates a number of clusters
def estimate_num_clusters_candidates(X:np.array, num_clusters_max:int=25, verbose:bool = False)->np.array:
    """
    Estimate candidates a number of clusters.
    X -- df or array of features.
    num_clusters_max -- Maximum number of clusters allowed (default, 25).
    verbose -- Display extra information (default, False).
    return -- Return candiates
    """
    # input validation
    assert type(X) is np.array or type(X) is np.ndarray, "It is required data container be a Numpy array."
    # list of possible clusters number values
    possible_k = np.arange(1,25,1)  
    # initialize
    ss = list()
    # loop of possible values
    for k in possible_k:
        # get labels of clustering
        labels = kmeans_labels(X, n_clusters=k)
        # get metric
        s = calinski_harabasz_score(X, labels)
        # validate metrix
        if np.isnan(s):
            s = 0.
        # append metric value  
        ss.append(s)
    # list to array
    ss = np.array(ss)
    # estimate local maximums to get number of cluster candidates
    num_clusters_metric = local_maximums_metric(possible_k, ss)
    # return all of candidates
    return num_clusters_metric, ss


## Plot clusters for the first and second PCs
def plot_cluster(X:pd.DataFrame, y:np.array, ax:"axes", title:str="Cluster plot")->"axes":
    """
    Plot clusters for the first and second PCs.
    X -- df of CPs to be plotted.
    y -- Array of labels to display extra information.
    ax -- Matplotlib axes to be used to plot the current chart.
    title -- Title to be add (default, "Cluster plot").
    return -- Matplotlib axes with the new chart included.
    """
    # scatter plot
    ax = X.plot.scatter(x=0, y=1, c=y, title = title, edgecolor='black', s=50, alpha = .5, colormap = 'jet', ax = ax)
    # set labels    
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    # set grid
    ax.xaxis.grid(True)
    ax.yaxis.grid(True)
    # return
    return ax


## Plot metric chart
def plot_metric(possible_k:np.array, array_metrics:np.array, ax:"axes", num_clusters_metric:np.array=None)->"axes":
    """
    Plot metric chart.
    possible_k -- Possible values of k (number of clusters).
    array_metrics -- Estimated metrics to be plotted.
    ax -- MatPlotLib axes where include the current chart.
    num_clusters_metrics -- k values to be candidates to be used on k-means.
    return -- MatPlotLib axes with the included chart.
    """
    # line chart
    ax.plot(possible_k, array_metrics, color = 'blue', alpha = .5)
    # scatter plot to mark stronger
    ax.scatter(possible_k, array_metrics, color = 'blue', edgecolor='black')
    # settings
    ax.set_ylim([np.min(array_metrics[array_metrics>0]-np.std(array_metrics[array_metrics>0])),np.max(array_metrics)+np.std(array_metrics[array_metrics>0])])
    ax.set_xticks(possible_k)
    ax.set_xticklabels(possible_k, rotation='horizontal',fontsize='small')
    ax.set_xlabel("number of clusters")
    ax.set_ylabel("Calinski Harabasz score")
    ax.set_title("Number of clusters selection")
    ax.xaxis.grid(True)
    ax.yaxis.grid(True)
    # mark candidates with vertical lines
    if not num_clusters_metric is None:
       for v in num_clusters_metric:
           ax.axvline(v, color='red', linestyle='--', alpha = .5)
    # return
    return ax


## Column type conversion to avoid problems with prince.FAMD
def type_conversion(df:pd.DataFrame)->pd.DataFrame:
    """
    Column type conversion to avoid problems with prince.FAMD .
    df -- df with columns to be converted.
    return -- converted df.
    """
    # loop of columns / types
    for v,t in df.dtypes.items():
        # validate type
        if t == "category":
            # type conversion: category to object
            df[v] = df[v].astype(str)
    # return
    return df


## ANALYSIS CLUSTERING with automatic PCA and number of clusters selection
def analysis_clustering(X:pd.DataFrame, y:pd.DataFrame = None,
                        is_rescale = True,
                        variance_threshold:float = .95,
                        position_cluster_selection = 0,
                        num_clusters_max = 25,
                        random_state = 42,
                        verbose = True)->np.array:
    """
    ANALYSIS CLUSTERING with automatic PCA and number of clusters selection
    X -- df of features to be analized.
    is_rescale -- If rescale before PCA for only numerical variables (default, True).    
    variance_threshold -- Value of cumulative variance to be used as limit (default, 0.95).
    position_cluster_selection -- Position to select between the  number of clusters candidates (default, 0). 
    num_clusters_max -- Maximum number of clusters allowed (default, 25).
    random_state -- Seed (default, 42).
    verbose -- Display extra information and charts (default, True).
    """
    # inpunt svalidation
    assert type(X) is pd.core.frame.DataFrame, "Input data is required stored in a Pandas df."
    assert 0 < variance_threshold <= 1., "Variance threshold value is required between 0 and 1."
    assert type(num_clusters_max) is int

    # type conversion: category to object and int to float
    X = type_conversion(X)
    # validate if is a mixed num / cat column s
    cols_num = X.select_dtypes(include=['float64', 'int64']).columns.tolist()
    if len(cols_num) != len(X.columns):
        is_mixed = True
        print("It is a mixed num / cat variables dataset.")
    else:
        is_mixed = False

    """ Dimensionality Reduction """

    # display
    print("\n\n-- DIMENSIONALITY REDUCTION ANALYSIS --\n")
    # number of pcs selection
    ncs = pca_number_pcs_auto_selection(X, variance_threshold, is_mixed, is_rescale, verbose)
    # dimensionality reduction initializaction
    rd = analysis_pca(X, y, n_components = ncs, is_mixed = is_mixed, is_rescale = is_rescale, random_state = random_state, verbose = verbose)
    X_pcs = rd.fit_transform(X)


    """ Clustering """

    # display
    print("\n\n-- CLUSTERING ANALYSIS --\n")
    # estimate candidates of number of clusters
    num_clusters_metric, ss = estimate_num_clusters_candidates(X_pcs.values, num_clusters_max, verbose)
    # validation
    if len(num_clusters_metric) == 0:
        print('[warning] There are not any possible number of cluster.')
        return None
    # display
    if verbose:
        print(f'Possible number of clusters to be selected = {num_clusters_metric}')
    # number of clusters value selection
    if position_cluster_selection < len(num_clusters_metric):
        num_clusters_selected = num_clusters_metric[position_cluster_selection]
    else:
        print(f'[error] There are not available any possible number of clusters value in the selected position = {position_cluster_selection}')
        return None
    # display
    if verbose:
        print(f'Selected optimal number of clusters = {num_clusters_selected}')
    # clustering
    model = KMeans(n_clusters = num_clusters_selected, random_state = random_state).fit(X_pcs)
    # get labels
    pred = model.labels_
    # plot
    if verbose:
        import matplotlib.pyplot as plt
        if num_clusters_selected < 10:
            fig, (ax1, ax2) = plt.subplots(ncols = 2, figsize = (16,6))
            ax1 = plot_cluster(X_pcs, pred, ax1, title=f"Number of clusters = {len(set(pred))}")
            ax2 = plot_metric(np.arange(1, num_clusters_max, 1), ss, ax2, num_clusters_metric)
        else:
            fig, ax = plt.subplots(ncols = 1, figsize = (8,6))
            ax = plot_metric(np.arange(1, num_clusters_max, 1), ss, ax, num_clusters_metric)            
        plt.show()
    # return labels     
    return pred