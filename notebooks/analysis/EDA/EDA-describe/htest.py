import numpy as np


## test if it is an array is a uniform distribution for numeric data
def test_uniform_num(data:np.array, alpha:float = .05, verbose:bool = False)->bool:
    """
    Test if it is an array is a uniform distribution for numeric data (Kolmogorov–Smirnov test).
    data -- 1D data to be tested.
    alpha -- Significance level (default, 0.05).
    verbose -- Display extra information (default, False).
    return -- boolean according test result.
    """
    from scipy.stats import uniform, ks_2samp
    # remove nan values
    data = data[~(np.isnan(data))]
    # get extremes
    dismin=np.amin(data)
    dismax=np.amax(data)
    # build an uniform distribution
    T=uniform(dismin,dismax-dismin).rvs(data.shape[0])
    # test if both have same distribution
    stat, p = ks_2samp(data, T)
    # display
    if verbose:
        print('stat=%.3f, p=%.3f' % (stat, p))
    # results
    if p > alpha:
        # display
        if verbose:
            print('Probably is Uniform')
        # return
        return True
    else:
        # display
        if verbose:
            print('Probably is not Uniform') 
        # return
        return False

    
## test if it is an array is a uniform distribution for categorial data    
def test_uniform_cat(data:np.array, alpha:float = .05, verbose:bool = False)->bool:
    """
    Test if it is an array is a uniform distribution for categorial data (Kolmogorov–Smirnov test).
    data -- 1D data to be tested.
    alpha -- Significance level (default, 0.05).
    verbose -- Display extra information (default, False).
    return -- boolean according test result.
    """
    from scipy.stats import ks_2samp
    # number of categories
    cats = np.unique(data)
    # resize if data is too large
    if len(data)>1000 and len(cats)*1000 < len(data):
        data = np.random.choice(data, size = len(cats)*1000)    
    # create artificial data with uniform distribution
    data_uniform = np.random.choice(cats, size = len(data), p = np.ones(len(cats)) / len(cats))
    # cat to num of input data
    temp = list()
    for ii, ic in enumerate(cats):
        temp += list(np.ones(len(data[data==ic])) * ii)
    data_modif = np.array(temp)
    # cat to num of artificial data
    temp = list()
    for ii, ic in enumerate(cats):
        temp += list(np.ones(len(data_uniform[data_uniform==ic])) * ii)
    data_uniform_modif = np.array(temp)
    # test
    stat, p = ks_2samp(data, data_uniform)
    if verbose:
        print('stat=%.3f, p=%.3f' % (stat, p))
    if p > alpha:
        if verbose:
            print('Probably is Uniform')
        return True
    else:
        if verbose:
            print('Probably is not Uniform')   
        return False

    
## test if distribution is Gaussian
def test_shapiro(data:np.array, alpha:float = .05, verbose:bool = False)->bool:
    """
    Test if distribution is Gaussian (Shapiro–Wilk test).
    data -- 1D data to be tested.
    alpha -- Significance level (default, 0.05).
    verbose -- Display extra information (default, False).
    return -- boolean according test result.
    """
    from scipy.stats import shapiro
    data = data[~(np.isnan(data))]
    stat, p = shapiro(data)
    if verbose:
        print('stat=%.3f, p=%.3f' % (stat, p))
    if p > alpha:
        if verbose:
            print('Probably Gaussian')
        return True
    else:
        if verbose:
            print('Probably not Gaussian')
        return False

    
## test if is unimodal
def test_dip(data:np.array, alpha:float = 0.05, verbose:bool = False)->bool:
    """
    Test if is unimodal (Hartigan’s test).
    data -- 1D data to be tested.
    alpha -- Significance level (default, 0.05).
    verbose -- Display extra information (default, False).
    return -- boolean according test result.
    """
    import unidip.dip as dip
    data = data[~(np.isnan(data))]
    # sort data
    data = np.msort(data)
    # test
    stat, p, _ = dip.diptst(data)
    if p is None:
        return np.nan
    # display
    if verbose:
        print('stat=%.3f, p=%.3f' % (stat, p))
    if p > alpha:
        if verbose:
            print('Probably unimodal')
        return True
    else:
        if verbose:
            print('Probably not unimodal.')
        return False
        