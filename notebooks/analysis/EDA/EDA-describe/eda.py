import pandas as pd
import numpy as np
import math
from scipy.stats import kurtosis, skew

## order of magnitude
def magnitude(value:float)->int:
    if (value == 0): return 0
    return int(math.floor(math.log10(abs(value))))

## most frequent value in a list
def most_frequent(List:list):
    return max(set(List), key = List.count)

## describe function for numeric data
def describe_numeric(data:pd.DataFrame)->pd.DataFrame:
    """
    Describe tool for numeric data.
    data -- dataframe with data to be described.
    return -- describe df.
    """
    # get names of numeric columns
    cols_num = data.select_dtypes(include=['float64', 'int64']).columns.values
    # describe
    dfn = data[cols_num].describe(include = 'all', percentiles = [.05, .25, .5, .75, .95]).T
    # add percent of nan values
    dfn['%nan'] = (data[cols_num].isnull().sum()*100 / len(data)).values
    # kurtosis
    dfn['kurtosis'] = kurtosis(data[cols_num])
    # skew
    dfn['skew'] = skew(data[cols_num])
    # order of magnitude
    dfn['magnitude'] = [most_frequent([magnitude(v) for v in data[c]]) for c in cols_num]
    # return
    return dfn

## describe function for categorical data
def describe_categorical(data:pd.DataFrame, max_size_cats:int = 5)->pd.DataFrame:
    """
    Describe tool for categorical data.
    data -- dataframe with data to be described.
    max_size_cats -- maximum number of categories to be showed.
    return -- describe df.
    """
    # get names of categorical columns
    cols_cat = data.select_dtypes(include=['object']).columns.values
    # describe
    dfc = data[cols_cat].describe(include = 'all').T[['count', 'unique']]
    # add percent of nan values
    dfc['%nan'] = (data[cols_cat].isnull().sum()*100 / len(data)).values
    
    ## add categories percents

    # set columns
    col_temp = ['var'] + ['value{}'.format(i) for i in range(max_size_cats)] + ['%value{}'.format(i) for i in range(max_size_cats)]
    # initialize
    values_temp = list()
    # loop of variables
    for col in cols_cat:
        # count categories
        temp = data[col].value_counts(normalize=True,sort=True,ascending=False)*100.
        # collect values and names
        c = temp.index.values
        v = temp.values
        # resize
        if len(v) > max_size_cats:
            v = np.append(v[:max_size_cats-1], np.sum(v[-(max_size_cats):]))
            c = np.append(c[:max_size_cats-1], 'others')
        else:
            v = np.pad(v,(0, max_size_cats-len(v)), 'constant', constant_values=np.nan)
            c = np.pad(c,(0, max_size_cats-len(c)), 'constant', constant_values=np.nan)
        # append    
        values_temp.append([col] + list(np.append(c,v)))
    # add new information
    dfc = pd.concat([dfc, pd.DataFrame(values_temp, columns = col_temp).set_index('var')], axis = 1)
    # return
    return dfc    