# @Author: juan
# @Date:   2019-01-16T08:49:20+01:00
# @Last modified by:   juan
# @Last modified time: 2019-01-16T08:49:20+01:00

import matplotlib.pyplot as plt
import seaborn as sns
import math
import warnings
warnings.filterwarnings('ignore')

"""
Plot histogram from the column of a dataframe. 
"""


## functions ##

## float to int truncating for possitive and negative values
def truncate(x:float)->int:
    return math.floor(x) if x<0 else math.ceil(x)


## main function ##

## plot histogram from df
def plot_from_df(df:'dataframe', colname:str, nbins:int = None, title:str = '', cumulative:bool = False, figsize:tuple = (8,4)):
	# number of bins
	if nbins is None:
		X = df[colname].values
		R = truncate(np.ptp(X))
		n = len(X)
		sigma = np.nanstd(X)
		nbins = truncate(( R * (n**float(1/3)) ) / 3.49 * sigma )

	# plot
	plt.figure(figsize=figsize)
	if cumulative: g = sns.distplot(df[[colname]],hist_kws=dict(cumulative=True),kde_kws=dict(cumulative=True))
	else: g = sns.distplot(df[[colname]], bins = nbins)
	g.set_title(title, fontsize=12)
	g.set_xlabel(colname)
	g.set_ylabel("freq", fontsize=10)
	plt.show()


if __name__ == '__main__':
	import numpy as np
	import pandas as pd

	""" data """

	# data creation
	N = 1000
	np.random.seed(1)
	X1 = np.concatenate((np.random.normal(0, 1, int(0.3 * N)),
	                    np.random.normal(5, 1, int(0.7 * N))))[:, np.newaxis]
	X2 = np.concatenate((np.random.normal(1, 1, int(0.3 * N)),
                    np.random.normal(3, 1, int(0.7 * N))))[:, np.newaxis]
	# to df
	df = pd.DataFrame({'col1':X1.ravel(), 'col2':X2.ravel()})


	""" plot """

	plot_from_df(df, 'col1')