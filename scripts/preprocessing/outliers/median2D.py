# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-09-25 17:03:26
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-09-25 17:25:22

"""
Outilers identifier for 2D data based on Median Absolute Deviation of RESIDUES.
"""

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import r2_score
import numpy as np


def _get_median_residues(signal: 'array', threshold: float, isreplace: bool =False):
    """
    Filter based on Median Absolute Deviation technique.
    signal -- signal to be filtered.
    threshold -- threshold.
    isreplace -- if it is True, replace identified outliers per the
                median of the signal. If it is False, is inputed as
                Nan (default False).
    returns: filtered signal where outliers have been inputed.
    """
    # identify outliers
    difference = np.abs(signal - np.nanmedian(signal))
    median_difference = np.nanmedian(difference)
    s = 0 if median_difference == 0 else difference / float(median_difference)
    mask = s > threshold
    # validate if smallest residues are inputed as outliers
    iback = np.where((mask) & (signal < np.nanmedian(signal)))[0]
    if len(iback) > 0:
        mask[iback] = False
    # inpute outliers
    if isreplace:
        signal[mask] = np.nanmedian(signal)  # replace
    else:
        signal[mask] = np.nan                       # delete
    return signal


def launch(x1: 'array', x2: 'array', percent: float = 20., isplot: bool = False):
    """
    Outilers identifier for 2D data.
    x1 -- array of the first variable.
    x2 -- array of the second variable.
    percent -- maximum percent of data to be filtered (default 20%).
    isplot -- plor or not results (default False)
    return -- isoutlier mask array with True/False values.
    """

    # prepare data
    X = np.c_[x1, x2]
    #  min max scaler
    scaler = MinMaxScaler()
    X_t = scaler.fit_transform(X)
    signal = np.abs(X_t[:, 0] - X_t[:, 1])
    # looking for outliers
    for ith in np.arange(0., 5., 0.1):
        signal_filtered = _get_median_residues(signal.copy(), ith)
        ilout = np.where(np.isnan(signal_filtered))[0]
        ilin = np.where(np.isnan(signal_filtered) == False)[0]
        p = len(ilout)*100/len(signal)
        vr2 = r2_score(X_t[ilin, 0], X_t[ilin, 1])
        if p < percent:
            print('[info] threshold = %s / num. outliers(total) = %s(%s) / percent of filtered data: %.3f %s / r2 score = %.3f' %
                  (ith, len(ilout), len(signal), p, '%', vr2))
            break
    # validation
    if len(ilin) <= 50.:
        print('[warning] the set of filtered data is too small: len(x) = %s .' % (len(ilin)))
    if vr2 < 0.5:
        print('[warning] the set of filtered data has got a poor correlation: r2 score = %.3f .' % (vr2))

    # plot
    if isplot:
        import matplotlib.pyplot as plt
        fig = plt.figure(figsize=(20, 5))
        # trend of residules
        ax1 = plt.subplot2grid((1, 4), (0, 0), colspan=3)
        x = np.arange(len(signal))
        y0 = signal
        y1 = signal_filtered
        ax1.plot(x, y0, 'b--')
        ax1.scatter(x, y0, color='red')
        ax1.scatter(x, y1, color='blue')
        ax1.set_title('Residues')
        ax1.set_xlabel("time")
        ax1.set_ylabel("abs(residue)")
        # scatter of 2d filtering
        ax2 = plt.subplot2grid((1, 4), (0, 3))
        ax2.scatter(X[:, 0], X[:, 1], color='blue')
        ax2.scatter(X[ilout, 0], X[ilout, 1], color='red')
        ax2.set_title('Outliers')
        ax2.set_xlabel("v1")
        ax2.set_ylabel("v2")
        # adjust and display
        plt.subplots_adjust(wspace=0.3)
        plt.show()
    # return
    isoutlier = np.ones(len(signal)) * False
    isoutlier[ilout] = True
    return isoutlier
