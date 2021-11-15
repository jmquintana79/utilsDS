#!/usr/bin/env python
# coding: utf-8

# # ADA (Automatic Data Analysis) - Univariate


import warnings
warnings.filterwarnings('ignore')
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import itertools

from analysis import sample_size
from analysis import analysis_normality
from analysis import analysis_correlation
from classes import Columns, Report
from data import data_simplify, remove_outliers
from tools import thresholds_according_level_exigence, check_is_enough_data


#%% parameters

# exigence level
exigence_level = 'normal'

#%% LOAD DATA

# load dataset
dataset = load_iris()
dataset.keys()
# dataset to df
raw = pd.DataFrame(dataset.data, columns = dataset.feature_names)
raw['class'] = dataset.target
dclass = dict()
for i, ic in enumerate(dataset.target_names):
    dclass[i] = ic
raw['class'] = raw['class'].map(dclass)


#%% DATA PREPARATION


# initialize report
REPORT = Report()
# dataset simplification
data, dcols_alias_to_name, d_converter_cat_values = data_simplify(raw)

# level of exigence
dexigence = thresholds_according_level_exigence(exigence_level)

#%% remove outliers in numerical columns

# get columns
cols = Columns(data)
# loop of num columns
for c in cols.num:
    # remove outliers (JUAN: hay que incluir reports en el sistema)
    data, ireports = remove_outliers(data, c, verbose = True)
    # add to report
    REPORT.add(ireports)
    # clean
    del ireports


#%% queries combinations


# add more categorical variables [PARA TESTING]
#data['c1'] = data['n1'].apply(lambda x: str(int(x)))
#data['c2'] = data['n2'].apply(lambda x: str(int(x)))


# initialize final lists with single queries
LIST_QUERIES = list()
LIST_INDEX = list()
# initialize
n = 0
cols = Columns(data)

## variables combination

# all possible combinations between variables
per_cols = list()
for i in range(1,len(cols.cat)+1,1):
    per_cols += list(itertools.permutations(list(cols.cat),r=i))

## singles queries

# initialize
dsingle_queries = dict()
# get single queries
for iper_cols in per_cols:
    dsingle_queries[iper_cols[0]] = [f"{iper_cols[0]} == '{cat}'" for cat in sorted(list(data[iper_cols[0]].unique()))]

# loop of single queries
for c in dsingle_queries:
    # add single queries
    LIST_QUERIES += dsingle_queries[c]
    # add their indexes
    LIST_INDEX += [n for i in range(len(dsingle_queries[c]))]
    # add to index
    n+=1
    
## non single queries

# get combination queries
for iper_cols in [pc for pc in per_cols if len(pc)>1]:
    # combine list of single queries
    isingle_queries = list()
    for c in iper_cols:
        isingle_queries += dsingle_queries[c]
    # get all possible combinations
    comb = list(itertools.combinations(isingle_queries,r=len(iper_cols)))
    # initialize
    final_comb = list()
    # loop of combinations
    for ic in comb:
        # create final query
        icomb = ' & '.join(ic)
        # append only necessary queries
        if np.prod([c in icomb for c in iper_cols]):
            final_comb.append(icomb)
    # sort and append to the final list
    final_comb = sorted(final_comb)
    LIST_QUERIES += final_comb
    
    # estimate their indexes
    l = [c.split(f' & {iper_cols[-1]}')[:-1] for c in final_comb]
    ln = [n]
    for i in range(len(l)-1):
        if l[i] != l[i+1]:
            n += 1
        ln.append(n) 
    # add indexes to the final list
    LIST_INDEX += ln
    
# store queries in a df
dfqueries = pd.DataFrame({'query':LIST_QUERIES, 'number':LIST_INDEX})


## add number of records per query

# initialize
LIST_SIZES = list()
# loop of queries
for squery in dfqueries['query'].values:
    LIST_SIZES.append(len(data.query(squery)))
# add new columnt
dfqueries['sample_size'] = LIST_SIZES


## Filter queries by min size of sample

# estimate minimun size of sample
population_sz = len(data)
confidence_level = (1. - dexigence['significance']) * 100.
confidence_interval = 5.0
n_min_sample_size = sample_size(population_sz, confidence_level, confidence_interval)
print("SAMPLE SIZE: %d from %d" %(n_min_sample_size, population_sz))
# FOR TESTING
n_min_sample_size = 50
# filter queries
dfqueries = dfqueries[dfqueries.sample_size>=n_min_sample_size]
print(f'Number of queries after filtering = {len(dfqueries)}')


#%% ANALYSIS

# get combinations of numerical variables (JUAN: en este caso solo combinaciones num - num)
comb_num_num = list(itertools.combinations(list(cols.num),r=2))

# get set of queries
numbers_query_sets = sorted(list(dfqueries['number'].unique()))

# loop of numbers of query sets
number = numbers_query_sets[0] # JUAN: in this case the first set

# get queries for this set
queries = dfqueries[dfqueries['number'] == number]['query'].tolist()

# get variables to remove of being analysed (JUAN in this case only numerical)
cols_all = data.columns.tolist()
cols_remove = [c for c in cols_all if c in queries[0]]
cols_num = [c for c in cols.num if not c in cols_remove]

# initialize samples
dsamples = dict()

# get samples per set
for squery in queries[:1]:
    # get sample
    dsamples[squery] = data.query(squery)[cols_num]
    


#%% num - num (entre columnas)
# 
# - https://datascience.stackexchange.com/questions/64260/pearson-vs-spearman-vs-kendall/64261





#%% full dataset

# normality test for numerical variables
dnormality, lreports = analysis_normality(data, list(cols.num), dexigence['significance'])
# add reports
if len(lreports) > 0:
    REPORT.add(lreports)

# loop of combinations
for comb in comb_num_num:
    # correlation analysis
    couple_columns = list(comb)
    corr = analysis_correlation(data, couple_columns, dnormality = dnormality, significance=dexigence['significance'], verbose = False)
    # chreck if add to report
    if np.abs(corr) >= dexigence['correlation']:
        # build report
        sreport = f'Correlation between "{comb[0]}" and "{comb[1]}" is {corr}'
        # add report
        REPORT.add(sreport)
        


"""

# validate if enough data / JUAN: stop analysis if is_enough is False
is_enough_var1 = check_is_enough_data(v1, n_min_sample_size)
is_enough_var2 = check_is_enough_data(v2, n_min_sample_size)
# normality test
if is_enough_var1:
    is_normal1, report1 = analysis_normality(v1, dexigence['significance'])
    if is_normal1:
        REPORT.add(f'"{col_x[0]}": '+ report1)
if is_enough_var2:
    is_normal2, report2 = analysis_normality(v2, dexigence['significance'])
    if is_normal2:
        REPORT.add(f'"{col_x[1]}": '+ report2)
"""




#%% for one sample




