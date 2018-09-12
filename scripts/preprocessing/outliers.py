# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-09-12 16:41:39
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-09-12 17:33:25

import numpy as np
from pandas import read_csv
from scipy.stats import multivariate_normal


def estimateGaussian(dataset):
    mu = np.mean(dataset, axis=0)
    sigma = np.cov(dataset.T)
    return mu, sigma


def multivariateGaussian(dataset, mu, sigma):
    p = multivariate_normal(mean=mu, cov=sigma)
    return p.pdf(dataset)

# outliers detection using a Multi-Gaussian method


def outliers_multigaussian(data: 'df', threshold: float, snamex: str, snamey: str, isdeep: bool=False)->tuple:
    """
    Outliers detection using a Multi-Gaussian method.
    data -- dataframe with the columns to be checked.
    threshold -- threshold to be used to select the anomalous data.
    snamex -- column name of the first column data.
    snamey -- column name of the second column data.
    isdeep -- display or not information and draw a plot (default False)
    return -- tuple(dataframe with a new column 'isoutlier' where is labeled outliers / non outliers., basic info into a dict)
    """

    # validate column name arguments
    if not snamex in data.columns.tolist():
        print('[error] "%s" column do not exists into the dataframe.' % snamex)
        return None
    if not snamey in data.columns.tolist():
        print('[error] "%s" column do not exists into the dataframe.' % snamey)
        return None

    # df to array
    tr_data = data[[snamex, snamey]].as_matrix()

    # dimessions
    n_samples = tr_data.shape[0]
    n_dim = tr_data.shape[1]
    if isdeep:
        print('[info] Number of datapoints: %d' % n_samples)
        print('[info] Number of dimensions/features: %d' % n_dim)
        print('[info] Outliers will be identify according to "%s" and "%s"' % (snamex, snamey))

    # calculate multivariable gaussian distribution
    mu, sigma = estimateGaussian(tr_data)
    p = multivariateGaussian(tr_data, mu, sigma)

    # selecting outlier datapoints
    outliers = np.asarray(np.where(p < threshold))

    # display
    if isdeep:
        print('[info] Threshold = %s' % threshold)
        print('[info] Number of Outliers = %s (%.3f%s)' % (len(outliers[0]), len(outliers[0])*100./n_samples, '%'))
    # store information
    dinfo = {'threshold': threshold, 'num_outliers': len(outliers[0]), 'percent_outliers': len(outliers[0])*100./n_samples}

    # set label of is outlier or not
    data['isoutlier'] = np.ones(n_samples) * False
    data['isoutlier'].iloc[outliers[0]] = np.ones(len(outliers[0])) * True
    data['isoutlier'] = data['isoutlier'].astype(int)

    # store final chart
    if isdeep:
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(5, 5))
        plt.xlabel('%s' % snamex)
        plt.ylabel('%s' % snamey)
        plt.plot(tr_data[:, 0], tr_data[:, 1], 'bx')
        plt.plot(tr_data[outliers, 0], tr_data[outliers, 1], 'ro')
        plt.title('Number of Outliers = %s (%.3f%s)\nThreshold = %s' %
                  (len(outliers[0]), len(outliers[0])*100./n_samples, '%', threshold), fontsize=14)
        ax.set_xlim([0., 1.])
        ax.set_ylim([0., 1.])
        plt.plot()
    # return
    return (data, dinfo)
