# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-12-03 16:57:06
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-12-03 17:28:57

# ERROR ANALYSIS
from tools.columns import num2cal
import warnings
from models.metrics import metrics_regression
import pandas as pd
import numpy as np
import sys
sys.path.append('../../')
warnings.filterwarnings('ignore')


# ## PLOT: Total Metrics

def total_metrics(data: 'df', sobservation: str, sprediction: str, nX=None):
    """
    Plot an error analysis overview for whole data.
    data -- df where is included the data to be validated.
    sobservation -- column name of real data.
    sprediction -- column name of predicted data.
    nX -- number of features used to calculate the prediction (default None).
    """

    # calculate total metrics
    dmetrics = metrics_regression(data[sobservation].values, data[sprediction].values, k=nX)
    bias, mae, r2 = dmetrics['bias'], dmetrics['mae'], dmetrics['r2']
    # calculate residues
    residues = data[sobservation].values - data[sprediction].values
    res_avg, res_std = np.mean(residues), np.std(residues)

    # PLOT 1
    import matplotlib.pyplot as plt
    import scipy.stats as stats
    fig = plt.figure(figsize=(15, 10))
    # pie1: BIAS
    ax1 = plt.subplot2grid((2, 3), (0, 0))
    labels = '%.3f' % bias, ''
    sizes = [np.abs(bias)*100./np.max(data[sobservation].values),
             (np.max(data[sobservation].values) - np.abs(bias))*100. / np.max(data[sobservation].values)]
    explode = (0.1, 0)
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.3f%%', shadow=False, startangle=65,
            textprops=dict(fontsize=18), colors=['red', 'yellow'])
    ax1.axis('equal')
    ax1.set_title("BIAS", fontsize=18)

    # pie2: MAE
    ax2 = plt.subplot2grid((2, 3), (0, 1))
    labels = '%.3f' % mae, ''
    sizes = [np.abs(mae)*100./np.max(data[sobservation].values),
             (np.max(data[sobservation].values) - np.abs(mae))*100. / np.max(data[sobservation].values)]
    explode = (0.1, 0)
    ax2.pie(sizes, explode=explode, labels=labels, autopct='%1.3f%%', shadow=False, startangle=65,
            textprops=dict(fontsize=18), colors=['red', 'purple'])
    ax2.axis('equal')
    ax2.set_title("MAE", fontsize=18)

    # pie3: R2
    ax3 = plt.subplot2grid((2, 3), (0, 2))
    labels = '%.3f' % r2, ''
    sizes = [np.abs(r2)*100, (1 - np.abs(r2))*100.]
    explode = (0.1, 0)
    ax3.pie(sizes, explode=explode, labels=labels, autopct='%1.3f%%', shadow=False, startangle=265,
            textprops=dict(fontsize=18), colors=['green', 'red'])
    ax3.axis('equal')
    ax3.set_title("R2", fontsize=18)

    # scatter: RESIDUES vs Y
    ax4 = plt.subplot2grid((2, 3), (1, 0))
    bins = np.linspace(min(residues), max(residues), 50)
    ax4.scatter(data[sobservation].values, residues, s=10, facecolors='none', edgecolors='black')
    ax4.hlines(res_avg,
               np.min(data[sobservation].values), np.max(data[sobservation].values),
               colors='red', linestyles='solid', label='average')
    ax4.hlines(res_avg + res_std,
               np.min(data[sobservation].values), np.max(data[sobservation].values),
               colors='red', linestyles='--', label='std')
    ax4.hlines(res_avg - res_std,
               np.min(data[sobservation].values), np.max(data[sobservation].values),
               colors='red', linestyles='--')
    ax4.legend(loc='best', fontsize=12, shadow=True)
    ax4.set_title("RESIDUES = %.3f +/- %.3f" % (res_avg, res_std), fontsize=18)
    ax4.set_xlabel(sobservation, fontsize=14)
    ax4.set_ylabel('')
    ax4.set_facecolor('xkcd:white')

    # probplot: RESIDUES (vs theoretical Norm distribution)
    ax5 = plt.subplot2grid((2, 3), (1, 1))
    stats.probplot(residues, dist="norm", plot=ax5, fit=True)
    ax5.set_title("Probplot: RESIDUES\n(vs Norm Dist.)", fontsize=18)
    ax5.set_xlabel('Theoretical Quantiles', fontsize=14)
    ax5.set_ylabel('Ordered Values', fontsize=14)

    # display
    plt.subplots_adjust(wspace=0.5)
    plt.show()


# ## PLOT: Metrics according to a reference categorical variable

def per_reference_metrics(data: 'df', sobservation: str, sprediction: str, sreference: str, nX=None):
    """
    Plot metrics per each value of a reference categorical variable.
    data -- df where is included the data to be validated.
    sobservation -- column name of real data.
    sprediction -- column name of predicted data.
    sreference -- column name of the reference variable.
    nX -- number of features used to calculate the prediction (default None).
    """

    # METRICS CALCULATION

    lvar_values = sorted(data[sreference].unique())
    # by values of reference variable
    lbias = list()
    lmae = list()
    lr2 = list()
    lres_avg = list()
    lres_std = list()
    lfolk = list()
    for ivar_value in lvar_values:
        # collect data
        idata = data[data[sreference] == ivar_value]
        # calculate metrics
        dmetrics = metrics_regression(idata[sobservation].values, idata[sprediction].values, k=nX)
        ibias, imae, ir2 = dmetrics['bias'], dmetrics['mae'], dmetrics['r2']
        # calculate residues
        iresidues = idata[sobservation].values - idata[sprediction].values
        ires_avg, ires_std = np.mean(iresidues), np.std(iresidues)
        # store
        lfolk.append(ivar_value)
        lbias.append(ibias)
        lmae.append(imae)
        lr2.append(ir2)
        lres_avg.append(ires_avg)
        lres_std.append(ires_std)
    resfolk = pd.DataFrame({
        sreference: lfolk,
        'bias': lbias,
        'mae': lmae,
        'r2': lr2,
        'res_avg': lres_avg,
        'res_std': lres_std
    }).set_index(sreference)
    # drop inf values
    resfolk = resfolk.replace([np.inf, -np.inf], np.nan)

    # PLOT PER THE REFERENCE VARIABLE
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(20, 15))

    # line: BIAS
    ax1 = plt.subplot2grid((5, 1), (0, 0))
    ax1.plot(resfolk.index.tolist(), resfolk.bias.tolist(), linestyle='--', color='blue', linewidth=3)
    ax1.scatter(resfolk.index.tolist(), resfolk.bias.tolist(), color='blue')
    for i, v in enumerate(resfolk.bias.values):
        if not np.isnan(v):
            ax1.annotate('%.3f' % v, (i, v), fontsize=14, rotation=45, color='grey')
    ax1.set_title('BIAS', fontsize=18)
    ax1.set_xticks(resfolk.index.tolist())
    ax1.set_xticklabels(resfolk.index.tolist(), fontsize=14)

    # line: MAE
    ax2 = plt.subplot2grid((5, 1), (1, 0))
    ax2.plot(resfolk.index.tolist(), resfolk.mae.tolist(), linestyle='--', color='orange', linewidth=3)
    ax2.scatter(resfolk.index.tolist(), resfolk.mae.tolist(), color='orange')
    for i, v in enumerate(resfolk.mae.values):
        if not np.isnan(v):
            ax2.annotate('%.3f' % v, (i, v), fontsize=14, rotation=45, color='grey')
    ax2.set_title('MAE', fontsize=18)
    ax2.set_xticks(resfolk.index.tolist())
    ax2.set_xticklabels(resfolk.index.tolist(), fontsize=14)

    # line: R2
    ax3 = plt.subplot2grid((5, 1), (2, 0))
    ax3.plot(resfolk.index.tolist(), resfolk.r2.tolist(), linestyle='--', color='green', linewidth=3)
    ax3.scatter(resfolk.index.tolist(), resfolk.r2.tolist(), color='green')
    for i, v in enumerate(resfolk.r2.values):
        if not np.isnan(v):
            ax3.annotate('%.3f' % v, (i, v), fontsize=14, rotation=45, color='grey')
    ax3.set_title('R2', fontsize=18)
    ax3.set_xticks(resfolk.index.tolist())
    ax3.set_xticklabels(resfolk.index.tolist(), fontsize=14)
    ax3.set_ylim([0, 1])

    # line: RESIDUES(avg)
    ax4 = plt.subplot2grid((5, 1), (3, 0))
    ax4.plot(resfolk.index.tolist(), resfolk.res_avg.tolist(), linestyle='--', color='red', linewidth=3)
    ax4.scatter(resfolk.index.tolist(), resfolk.res_avg.tolist(), color='red')
    for i, v in enumerate(resfolk.res_avg.values):
        if not np.isnan(v):
            ax4.annotate('%.3f' % v, (i, v), fontsize=14, rotation=45, color='grey')
    ax4.set_title('RESIDUES (avg)', fontsize=18)
    ax4.set_xticks(resfolk.index.tolist())
    ax4.set_xticklabels(resfolk.index.tolist(), fontsize=14)

    # line: RESIDUES(std)
    ax5 = plt.subplot2grid((5, 1), (4, 0))
    ax5.plot(resfolk.index.tolist(), resfolk.res_std.tolist(), linestyle='--', color='red', linewidth=3)
    ax5.scatter(resfolk.index.tolist(), resfolk.res_std.tolist(), color='red')
    for i, v in enumerate(resfolk.res_std.values):
        if not np.isnan(v):
            ax5.annotate('%.3f' % v, (i, v), fontsize=14, rotation=45, color='grey')
    ax5.set_title('RESIDUES (std)', fontsize=18)
    ax5.set_xlabel(sreference, fontsize=14)
    ax5.set_xticks(resfolk.index.tolist())
    ax5.set_xticklabels(resfolk.index.tolist(), fontsize=14)

    # display
    plt.subplots_adjust(hspace=0.6)
    plt.show()
