import numpy as np
import pandas as pd
from tools import remove_outliers_IQR


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

    
## test if distribution is Gaussian (for N < 5000)
def test_shapiro(data:np.array, alpha:float = .05, verbose:bool = False)->bool:
    """
    Test if distribution is Gaussian (Shapiro–Wilk test).
    data -- 1D data to be tested.
    alpha -- Significance level (default, 0.05).
    verbose -- Display extra information (default, False).
    return -- boolean according test result.
    """
    from scipy.stats import shapiro
    # remove nan values
    data = data[~(np.isnan(data))]
    # test
    stat, p = shapiro(data)
    # display
    if verbose:
        print('stat=%.3f, p=%.3f' % (stat, p))
    # results
    if p > alpha:
        # display
        if verbose:
            print('Probably Gaussian')
        # return
        return True
    else:
        # display
        if verbose:
            print('Probably not Gaussian')
        # return
        return False

    
## test if distribution is Gaussian (large sample size) 
def test_anderson(data:np.array, alpha:float = .05, verbose:bool = False)->bool:
    """
    Test if distribution is Gaussian (Agostino and Pearson’s test).
    data -- 1D data to be tested.
    alpha -- Significance level (default, 0.05).
    verbose -- Display extra information (default, False).
    return -- boolean according test result.
    """
    from scipy.stats import normaltest
    # remove nan values
    data = data[~(np.isnan(data))]
    # test
    stat, p = normaltest(data)
    # display
    if verbose:
        print('stat=%.3f, p=%.3f' % (stat, p))
    # results
    if p > alpha:
        # display
        if verbose:
            print('Probably Gaussian')
        # return
        return True
    else:
        # display
        if verbose:
            print('Probably not Gaussian')
        # return
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


## Test if two numerical variables are independents (Pearson's)
def correlation_pearson(data1:np.array, data2:np.array, alpha:float = 0.05, verbose:bool = False)->bool:
    """
    Test if two numerical variables are independents (Pearson's).
    data1, date2 -- 1D data to be tested.
    alpha -- Significance level (default, 0.05).
    verbose -- Display extra information (default, False).
    return -- boolean according test result.
    """
    from scipy.stats import pearsonr
    # calculate Pearson's correlation
    corr, p = pearsonr(data1, data2)
    # display
    if verbose:
        print('stat=%.3f, p=%.3f' % (stat, p))
    # check result and return
    if p > alpha:
        # display
        if verbose:
            print('Probably independent')
        # return
        return True
    else:
        # display
        if verbose:
            print('Probably dependent')
        # return
        return False 
    
    
## Test if two numerical variables are independents (Spearman's)
def correlation_spearman(data1:np.array, data2:np.array, alpha:float = 0.05, verbose:bool = False)->bool:
    """
    Test if two numerical variables are independents (Spearman's).
    data1, date2 -- 1D data to be tested.
    alpha -- Significance level (default, 0.05).
    verbose -- Display extra information (default, False).
    return -- boolean according test result.
    """
    from scipy.stats import spearmanr
    # calculate Pearson's correlation
    corr, p = spearmanr(data1, data2)
    # display
    if verbose:
        print('stat=%.3f, p=%.3f' % (stat, p))
    # check result and return
    if p > alpha:
        # display
        if verbose:
            print('Probably independent')
        # return
        return True
    else:
        # display
        if verbose:
            print('Probably dependent')
        # return
        return False 
    
# Apply independence test for random subsamples (Pearson's)
def correlation_sample(correlation_function:'function',
                        dfsample:pd.DataFrame, 
                        col1:str, col2:str, 
                        is_remove_outliers:bool = False, 
                        alpha:float = 0.05, 
                        verbose:bool = False): 
    """
    Apply independence test for random subsamples (Pearson's).
    correlation_function -- correlation function to be used.
    df -- data sample to be analized.
    col1, col2 -- numerical variables to be analized.
    is_remove_outliers -- remove or not outliers (default, False)
    alpha -- Significance level (default, 0.05).
    verbose -- Display extra information (default, False).
    return -- boolean according test result.
    """
    # validate column names
    assert col1 in dfsample.columns.tolist()
    assert col2 in dfsample.columns.tolist()
    # collect data
    data1 = dfsample[col1].values.copy()
    data2 = dfsample[col2].values.copy()
    # remove or not outliers
    if is_remove_outliers:
        data1 = remove_outliers_IQR(data1)
        data2 = remove_outliers_IQR(data2)
    # correlation test and return
    return correlation_function(data1, data2, alpha = alpha, verbose = verbose)


## Test if two categorical variables are independents (Chi-Squared Test)
def chi_square(data1:np.array, data2:np.array, alpha:float = 0.05, verbose:bool = False)->bool:
    """
    Test if two categorical variables are independents (Chi-Squared Test).
    data1, date2 -- 1D data to be tested.
    alpha -- Significance level (default, 0.05).
    verbose -- Display extra information (default, False).
    return -- boolean according test result.
    """
    from scipy.stats import chi2_contingency
    # contingence table
    table = pd.crosstab(data1, data2, margins = False).values
    # test
    stat, p, dof, expected = chi2_contingency(table)
    # display
    if verbose:
        print('stat=%.3f, p=%.3f' % (stat, p))
    # results
    if p > alpha:
        # display
        if verbose:
            print('Probably independent')
        # return 
        return True
    else:
        # display
        if verbose:
            print('Probably dependent')
        # return
        return False
    
    
## ANOVA tests
def ANOVA(*args, alpha:float = 0.05, verbose:bool = False)->bool:
    """
    The one-way ANOVA tests the null hypothesis that two or more groups have the same 
    population mean. The test is applied to samples from two or more groups, possibly 
    with differing sizes.
    *args -- n groups of samples.
    alpha -- Significance level (default, 0.05).
    verbose -- Display extra information (default, False).
    return -- True / False, samples have same distribution.
    """
    from scipy.stats import f_oneway
    # test
    stat, p = f_oneway(*args)
    # display
    if verbose:
        print('Statistics=%.3f, p=%.3f' % (stat, p))
    # interpret
    if p > alpha:
        # display
        if verbose:
            print(f'Same distributions (fail to reject H0 with alpha = {alpha})')
        # return
        return True
    else:
        # display
        if verbose:
            print(f'Different distributions (reject H0 with alpha = {alpha})')
        # return
        return False