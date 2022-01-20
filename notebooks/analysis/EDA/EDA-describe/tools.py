import math
import numpy as np


## estimate order of magnitude
def magnitude(value:float)->int:
    """
    Estimate order of magnitude.
    value -- value to be analized.
    return -- order of magnitude.
    """
    if (value == 0): return 0
    try:
        return int(math.floor(math.log10(abs(value))))
    except:
        return np.nan

## estimate most frequent value in a list
def most_frequent(List:list)->"element":
    """
    Estimate most frequent value in a list.
    List -- list to be analized.
    return -- most freq element
    """
    return max(set(List), key = List.count)


## remove outliers of a 1D array according to the Inter Quartile Range (IQR)
def remove_outliers_IQR(v:np.array, verbose:bool = False)->np.array:
    """
    Remove outliers of a 1D array according to the Inter Quartile Range (IQR).
    v -- array of values to be analyzed.
    verbose -- display extra information (default, False).
    return -- array of values after removing outliers.
    """
    # estimate boundary thresholds
    Q1 = np.quantile(v,0.25)
    Q3 = np.quantile(v,0.75)
    IQR = Q3 - Q1
    t_lower = Q1 - 1.5*IQR
    t_upper = Q3 + 1.5*IQR
    # display
    if verbose:
        print('Thresholds: lower = %.5f / upper = %.5f'%(t_lower, t_upper))
    # remove values outside of these thresholds and return
    v[v < t_lower] = np.nan
    v[v > t_upper] = np.nan
    # return
    return v