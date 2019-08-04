# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-09-19 13:17:03
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-09-19 13:19:36

"""
Reference: https://www.statsmodels.org/dev/generated/statsmodels.nonparametric.smoothers_lowess.lowess.html
"""


def launch(x: 'array', y: 'array', fraction: float=.2, isplot: bool = False):
    """
    LOWESS (Locally Weighted Scatterplot Smoothing)
    x -- x data.
    y -- y data.
    fraction -- between 0 and 1. The fraction of the data used when estimating each y-value (default 0.2).
    """

    from scipy.interpolate import interp1d
    import statsmodels.api as sm
    # local regression
    lowess = sm.nonparametric.lowess(y, x, frac=.2, missing='drop')
    # unpack the lowess smoothed points to their values
    lowess_x = list(zip(*lowess))[0]
    lowess_y = list(zip(*lowess))[1]
    # interpolation the different portions
    f = interp1d(lowess_x, lowess_y, bounds_error=False)
    xnew = sorted(list(set(x)))
    ynew = f(xnew)
    # plot
    if isplot:
        import matplotlib.pyplot as plt
        plt.plot(x, y, 'o')
        plt.plot(lowess_x, lowess_y, '*')
        plt.plot(xnew, ynew, '-')
        plt.title('Locally Weighted Scatterplot Smoothing')
        plt.show()
    # return
    return (xnew, ynew)
