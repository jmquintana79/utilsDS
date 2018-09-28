# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-09-25 17:19:24
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-09-26 17:44:38


"""
MEDIAN ABSOLUTGE DEVIATION:

Filtering technique (of outliers) based on the median absolute deviation (MAD) which allow detecting the variability of an univariate sample of quantitative data.

The median absolute deviation (MAD) is defined as the median of deviations from the median

MAD=mediani(|Xi−medianj(Xj)|)
and you can find out more about it here http://en.wikipedia.org/wiki/Median_absolute_deviation
"""


def launch(signal: 'array', threshold: float, isreplace: bool =False):
    """
    Filter based on Median Absolute Deviation technique.
    signal -- signal to be filtered.
    threshold -- threshold.
    isreplace -- if it is True, replace identified outliers per the
                median of the signal. If it is False, is inputed as
                Nan (default False).
    returns: filtered signal where outliers have been inputed.
    """
    import numpy as np
    difference = np.abs(signal - np.nanmedian(signal))
    median_difference = np.nanmedian(difference)
    s = 0 if median_difference == 0 else difference / float(median_difference)
    mask = s > threshold
    if isreplace:
        signal[mask] = np.nanmedian(signal)  # replace
    else:
        signal[mask] = np.nan                       # delete
    return signal
