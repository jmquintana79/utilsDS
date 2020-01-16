# @Author: juan
# @Date:   2019-01-16T08:49:20+01:00
# @Last modified by:   juan
# @Last modified time: 2019-01-16T08:49:20+01:00

"""
Plot histogram includen estimated density function results for three different
kernels.
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from distutils.version import LooseVersion
from scipy.stats import norm
from sklearn.neighbors import KernelDensity
# `normed` is being deprecated in favor of `density` in histograms
if LooseVersion(matplotlib.__version__) >= '2.1':
    density_param = {'density': True}
else:
    density_param = {'normed': True}
import math
import scipy.stats as stats
from scipy.signal import argrelextrema


## functions ##

## estimate local maximumns for the gaussian density
def local_maximums_kde_gaussian(data:'array', threshold_freq:'float')->'array':
    """
    Estimate local maximumns for the gaussian density.
    data -- 1D array.
    threshold_freq -- frequency (probability) limit to discard or not a spike as a local maximum.
    return -- list of values where there are local maximums.
    """

    ## histogram density estimation with kde 
    noise = data[~np.isnan(data)]
    density = stats.gaussian_kde(noise)
    n, x = np.histogram(noise, bins = 250 , density=True)
    ## local maxima (histogram peaks) estimation = steps values
    imaxi = argrelextrema(density(x), np.greater)
    # validate if all peaks are zero
    is_all_zeros = len(np.where(n[imaxi]<=threshold_freq)[0])==len(n[imaxi])
    if is_all_zeros: threshold_freq = -9999.
    # select peaks = steps values average
    steps_avg = x[imaxi[0][np.where(n[imaxi]>threshold_freq)[0]]]
    # return
    return steps_avg

## float to int truncating for possitive and negative values
def truncate(x:float)->int:
    """
    Float to int truncating for possitive and negative values.
    x - float to be truncated.
    return truncated int.
    """
    return math.floor(x) if x<0 else math.ceil(x)


## main function ##

## plot histogram with densities estimated by KDE using different kernels
def plot(X:'array', threshold_freq:float = 0.0001, nbins:int = None, figsize:tuple = (15,8), supply:bool = False)->tuple:
    """
    Plot histogram with densities estimated by KDE using different kernels.
    X -- 1D array of data.
    threshold_freq -- frequency (probability) limit to discard or not a spike as a local maximum  (default 0.0001).
    nbins -- number of bins to be set (default None). In case of not to being included it will be estimated (optimal case).
    figsize -- figure size (default (15, 8)).
    supply -- return or not ax object. (default False).
    return -- ((x/y values of histogram), (x/y values of density for gaussian kernel), list of values where there are local maximums)
    
    NOTE - if supply = True, furthermore it will be returned the axis object ax.
    """

    # estimate x limits
    add = truncate(np.ptp(X)) * 0.5 / 10.
    xmin = truncate(np.min(X)) - add if truncate(np.min(X)) < 0 else truncate(np.min(X)) + add
    xmax = truncate(np.max(X)) - add if truncate(np.max(X)) < 0 else truncate(np.max(X)) + add

    # estimate local maximum
    steps_avg = local_maximums_kde_gaussian(X.copy(), threshold_freq) 
    #print('local maximums (gaussian): %s'%steps_avg)

    # number of bins
    if nbins is None:
        R = truncate(np.ptp(X))
        n = len(X)
        sigma = np.nanstd(X)
        nbins = truncate(( R * (n**float(1/3)) ) / 3.49 * sigma )
    bins = np.linspace(truncate(np.min(X)), truncate(np.max(X)), nbins)

    # x for plot
    X_plot = np.linspace(truncate(np.min(X)), truncate(np.max(X)), 1000)[:, np.newaxis]

    # create fig/axes
    fig, ax = plt.subplots(figsize = figsize)
    # plot the input data distribution
    h_y, h_x, _ = ax.hist(X , density = True, bins = bins, color = 'grey', label = 'input distribution', alpha = 0.2)
    # settings
    colors = ['cornflowerblue', 'darkorange', 'navy']
    kernels = ['tophat', 'epanechnikov', 'gaussian']
    lw = 2
    # calculate kde and plot
    for color, kernel in zip(colors, kernels):
        kde = KernelDensity(kernel=kernel, bandwidth=0.5).fit(X)
        log_dens = kde.score_samples(X_plot)
        ax.plot(X_plot[:, 0], np.exp(log_dens), color=color, lw=lw,
                linestyle='-', label="kernel = '{0}'".format(kernel))
        # store gaussian results
        if kernel == 'gaussian':
            l_y = np.exp(log_dens)
            l_x = X_plot[:, 0]
    # set legend
    ax.legend(loc='upper left')
    # plot points on the botton
    if len(X) < 10000:
        ax.plot(X[:, 0], -0.005 - 0.01 * np.random.random(X.shape[0]), '+k')
    # plot estimated local maximuns
    for avg in steps_avg:
        ax.axvline(avg, color='k', linestyle='--')
    # set chart limits
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(-0.02, np.max(h_y) + 0.05)
    # set title
    ax.set_title("%s points / %s bins"%(len(X), nbins))
    # set labels
    ax.set_ylabel("freq")
    # display / return
    if supply:
        return ((h_x, h_y), (l_x, l_y), steps_avg, ax)
    else:
        plt.show()
        return ((h_x, h_y), (l_x, l_y), steps_avg)
    


if __name__ == '__main__':

	""" data """

	N = 1000
	np.random.seed(1)
	X = np.concatenate((np.random.normal(0, 1, int(0.3 * N)),
	                    np.random.normal(5, 1, int(0.7 * N))))[:, np.newaxis]


	""" plot """

	h, l, steps_avg = plot(X, figsize = (20,10))

