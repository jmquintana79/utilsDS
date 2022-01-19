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