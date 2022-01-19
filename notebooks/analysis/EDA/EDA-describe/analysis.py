import pandas as pd
import numpy as np
from scipy.stats import kurtosis, skew
from tools import magnitude, most_frequent
import htest

 
## get basic information of df variables
def info(data:pd.DataFrame, decimals:int = 2)->pd.DataFrame:
    """
    Get basic information of df variables.
    data -- df to be analyzed.
    decimals -- precission to be returned (default, 2).
    return -- dataframe with the collected information.
    """
    # copy data
    df = data.copy()
    # get names of numeric columns
    cols_num = df.select_dtypes(include=['float64']).columns.values
    # get names of categorical columns
    cols_cat = df.select_dtypes(include=['object', 'int64', 'category', 'bool']).columns.values
    # get types information
    dfinfo = pd.DataFrame({'variable':df.dtypes.index, 'dtype':df.dtypes.values}).set_index('variable')
    # estimate number of unique values for categorical variables
    dfinfo['unique'] = np.ones(len(dfinfo)) * np.nan
    for col in cols_cat:
        dfinfo.loc[col,'unique'] = len(df[col].unique())
    # estimate order of magnitude for numerical variables
    dfinfo['magnitude'] = np.ones(len(dfinfo)) * np.nan
    for col in cols_num:
        dfinfo.loc[col,'magnitude'] = most_frequent([magnitude(v) for v in df[col]])
    # estimate percent of nan values
    dfinfo['%nan'] = (df.isnull().sum()*100 / len(df)).values.round(decimals=decimals)
    # estimate number of records without nan values
    nrecords = list()
    for col in df.columns.tolist():
        nrecords.append(len(df[col].dropna()))
    dfinfo['num_records'] = nrecords
    # return
    return dfinfo.sort_values('unique', ascending = False)


## describe function for numeric data
def describe_numeric(df:pd.DataFrame, alpha:float = .05, decimals:int = 2)->pd.DataFrame:
    """
    Describe tool for numeric data.
    df -- dataframe with data to be described.
    alpha -- significance level (default, 0.05).
    decimals -- precission to be returned (default, 2).
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
    dfn['uniform'] = [htest.test_uniform_num(data[c], alpha = alpha) for c in cols_num]
    # test if it is gaussian
    dfn['gaussian'] = [htest.test_shapiro(data[c], alpha = alpha) for c in cols_num]
    # test if it is gaussian
    dfn['unimodal'] = [htest.test_dip(data[c], alpha = alpha) for c in cols_num]
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
    alpha -- significance level (default, 0.05).
    decimals -- precission to be returned (default, 2).
    return -- describe df.
    """
    # get names of categorical columns
    cols_cat = df.select_dtypes(include=['object', 'int64', 'category', 'bool']).columns.values
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
    dfc['uniform'] = [htest.test_uniform_cat(data[c].dropna().values, alpha = alpha) for c in cols_cat]
    
    
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