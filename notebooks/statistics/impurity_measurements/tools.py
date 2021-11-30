import numpy as np
import pandas as pd

def test_ks2(data1, data2):
    from scipy.stats import ks_2samp
    stat, p = ks_2samp(data1, data2)
    print('stat=%.3f, p=%.3f' % (stat, p))
    if p > 0.05:
        print('Probably the same distribution')
    else:
        print('Probably different distributions')
        
def test_uniform_num(data):
    from scipy.stats import uniform, ks_2samp
    dismin=np.amin(data)
    dismax=np.amax(data)
    T=uniform(dismin,dismax-dismin).rvs(data.shape[0])
    stat, p = ks_2samp(data, T)
    print('stat=%.3f, p=%.3f' % (stat, p))
    if p > 0.05:
        print('Probably is Uniform')
    else:
        print('Probably is not Uniform') 
        
def getExtremePoints(data, typeOfInflexion = None, maxPoints = None):
    """
    This method returns the indeces where there is a change in the trend of the input series.
    typeOfInflexion = None returns all inflexion points, max only maximum values and min
    only min,
    """
    a = np.diff(data)
    asign = np.sign(a)
    signchange = ((np.roll(asign, 1) - asign) != 0).astype(int)
    idx = np.where(signchange ==1)[0]

    if typeOfInflexion == 'max' and data[idx[0]] < data[idx[1]]:
        idx = idx[1:][::2]
        
    elif typeOfInflexion == 'min' and data[idx[0]] > data[idx[1]]:
        idx = idx[1:][::2]
    elif typeOfInflexion is not None:
        idx = idx[::2]
    
    # sort ids by min value
    if 0 in idx:
        idx = np.delete(idx, 0)
    if (len(data)-1) in idx:
        idx = np.delete(idx, len(data)-1)
    idx = idx[np.argsort(data[idx])]
    # If we have maxpoints we want to make sure the timeseries has a cutpoint
    # in each segment, not all on a small interval
    if maxPoints is not None:
        idx= idx[:maxPoints]
        if len(idx) < maxPoints:
            return (np.arange(maxPoints) + 1) * (len(data)//(maxPoints + 1))
    
    return idx

## Get pdf estimated with KDE for 1D data
def get_pdf_1d(v:np.array)->(np.array, np.array, np.array):
    """
    Get pdf estimated with KDE for 1D data.
    v - 1D data array.
    return - (x, pdf, local maximum)
    """
    # get x values
    x = np.linspace(v.min(),v.max(), v.shape[0])
    # get kde kernel
    from scipy import stats
    kernel = stats.gaussian_kde(v)    
    # get local maximum
    idx = getExtremePoints(kernel(x), typeOfInflexion='max')
    # return
    return x, kernel(x), idx
    
## Plot pdf estimated with KDE for 1D data
def plot_pdf_1d(v:np.array):
    # get pdf
    x, pdf_kde, local_max = get_pdf_1d(v)
    # plot
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize= (14, 6))
    ax.plot(x, pdf_kde, alpha = 0.8, label = f'Statsmodels CV maximum likelihood')
    for i in local_max:
        ax.scatter(x[i], pdf_kde[i], s= 40, c = 'red')
    for i in local_max:
        ax.annotate(f' Max = {round(x[i], 2)}', (x[i], pdf_kde[i]))
    plt.show()
    
def test_dip(data, alpha = 0.05, verbose = True)->bool:
    import unidip.dip as dip
    # sort data
    data = np.msort(data)
    # test
    stat, p, _ = dip.diptst(data)
    # display
    if verbose:
        print('stat=%.3f, p=%.3f' % (stat, p))
    if p > 0.05:
        print('Probably unimodal')
    else:
        print('Probably not unimodal.')
        
## Estimate 1d clusters with KDE
def get_1d_clusters_kde(v:np.array, verbose = True)->np.array:
    """
    Estimate 1d clusters with KDE.
    v -- data array to be used.
    verbose -- display extra information (default, True)
    result -- array of estimated labels.
    """
    
    # get pdf and local maximuns
    pdf_kde, x, local_max = get_pdf_1d(v)
    # display results
    num_modals = len(local_max)
    # display
    if verbose:
        print(f'number of modals = {num_modals}')
    # reshape data
    v = v.reshape(-1, 1)
    # KDE algorithm
    from sklearn.mixture import GaussianMixture
    gmm = GaussianMixture(num_modals, covariance_type='full', random_state=0).fit(v)
    # get cluster means
    cluster_means = [cm for cm in gmm.means_]
    # display
    if verbose:
        print(f'cluster means: {cluster_means}')
    # get labels
    labels = gmm.predict(v)
    # return
    return labels

## Plot 1d clusters
def plot_1d_clusters_kde(v, labels):
    """
    Plot 1d clusters.
    v -- original data.
    labels -- its respective clusters.
    """
    # data and labels to df
    result = pd.DataFrame({'data':v.ravel(), 'cluster': labels})
    # get unique values of clusters
    clusters = sorted(list(result.cluster.unique()))
    # plot
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    colors = ['green', 'blue', 'red', 'yellow', 'orange', 'grey']
    for cluster, color in zip(clusters, colors[:len(clusters)]):
        temp = result[result.cluster == cluster]
        iv = temp.data.values
        ax.hist(iv, color = color, alpha = 0.5)
        del iv
    ax.set_title(f'number of clusters = {len(clusters)}')
    plt.show()
    
