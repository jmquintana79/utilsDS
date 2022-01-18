import pandas as pd
import numpy as np
import math
from scipy.stats import kurtosis, skew

## order of magnitude
def magnitude(value:float)->int:
    if (value == 0): return 0
    try:
        return int(math.floor(math.log10(abs(value))))
    except:
        return np.nan

## most frequent value in a list
def most_frequent(List:list):
    return max(set(List), key = List.count)

## test if it is an array is a uniform distribution for numeric data
def test_uniform_num(data:np.array, alpha:float = .05, verbose:bool = False)->bool:
    from scipy.stats import uniform, ks_2samp
    data = data[~(np.isnan(data))]
    dismin=np.amin(data)
    dismax=np.amax(data)
    T=uniform(dismin,dismax-dismin).rvs(data.shape[0])
    stat, p = ks_2samp(data, T)
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

## test if it is an array is a uniform distribution for categorial data    
def test_uniform_cat(data:np.array, alpha:float = .05, verbose:bool = False)->bool:
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
        
        
## describe function for numeric data
def describe_numeric(df:pd.DataFrame, alpha:float = .05, decimals:int = 2)->pd.DataFrame:
    """
    Describe tool for numeric data.
    df -- dataframe with data to be described.
    return -- describe df.
    """
    # get names of numeric columns
    cols_num = df.select_dtypes(include=['float64']).columns.values
    # copy data
    data = df[cols_num].copy()
    # describe
    dfn = data[cols_num].describe(include = 'all', percentiles = [.05, .25, .5, .75, .95]).T
    # add percent of nan values
    dfn['%nan'] = (data[cols_num].isnull().sum()*100 / len(data)).values
    # kurtosis
    dfn['kurtosis'] = kurtosis(data[cols_num], nan_policy = 'omit')
    # skew
    dfn['skew'] = skew(data[cols_num], nan_policy = 'omit')
    # order of magnitude
    dfn['magnitude'] = [most_frequent([magnitude(v) for v in data[c]]) for c in cols_num]
    # test if it is uniform
    dfn['uniform'] = [test_uniform_num(data[c], alpha = alpha) for c in cols_num]
    # test if it is gaussian
    dfn['gaussian'] = [test_shapiro(data[c], alpha = alpha) for c in cols_num]
    # test if it is gaussian
    dfn['unimodal'] = [test_dip(data[c], alpha = alpha) for c in cols_num]
    # format
    dfn['count'] = dfn['count'].astype(int)
    for col in ['mean', 'std', 'min', '5%', '25%', '50%', '75%', '95%', 'max','%nan', 'kurtosis', 'skew']:
        dfn[col] = dfn[col].values.round(decimals=decimals)
    # return
    return dfn

## describe function for categorical data
def describe_categorical(df:pd.DataFrame, max_size_cats:int = 5, alpha:float = .05, decimals:int = 2)->pd.DataFrame:
    """
    Describe tool for categorical data.
    df -- dataframe with data to be described.
    max_size_cats -- maximum number of categories to be showed.
    return -- describe df.
    """
    # get names of categorical columns
    cols_cat = df.select_dtypes(include=['object', 'int64', 'category']).columns.values
    # copy data
    data = df[cols_cat].copy()
    # integer to categorical
    for col in data.select_dtypes(include=['int64']).columns.values:
        data[col] = pd.Categorical(data[col])
    # describe
    dfc = data[cols_cat].describe(include = 'all').T[['count', 'unique']]
    # add percent of nan values
    dfc['%nan'] = (data[cols_cat].isnull().sum()*100 / len(data)).values.round(decimals=decimals)
    # test if it is uniform
    dfc['uniform'] = [test_uniform_cat(data[c].dropna().values, alpha = alpha) for c in cols_cat]
    
    
    ## add categories percents

    # set columns
    col_temp = ['var'] + ['value{}'.format(i) for i in range(max_size_cats)] + ['%value{}'.format(i) for i in range(max_size_cats)]
    # initialize
    values_temp = list()
    # loop of variables
    for col in cols_cat:
        # count categories
        temp = data[col].value_counts(normalize=True,sort=True,ascending=False,dropna=True)*100.
        # collect values and names
        c = temp.index.values
        v = temp.values.round(decimals=decimals)   
        # resize
        if len(v) > max_size_cats:
            v = np.append(v[:max_size_cats-1], np.sum(v[-(max_size_cats):]).round(decimals=decimals))
            c = np.append(c[:max_size_cats-1], 'others')
        else:
            v = np.pad(v.astype(str),(0, max_size_cats-len(v)), 'empty')
            c = np.pad(c.astype(str),(0, max_size_cats-len(c)), 'empty')
        # append    
        values_temp.append([col] + list(np.append(c,v)))
    # add new information
    dfc = pd.concat([dfc, pd.DataFrame(values_temp, columns = col_temp).set_index('var')], axis = 1)
    # return
    return dfc    