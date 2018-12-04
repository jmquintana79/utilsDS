# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-12-03 16:57:06
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-12-04 15:37:55

from sklearn.metrics import classification_report, recall_score, precision_score, f1_score
"""
ERROR ANALYSIS for categorical predictions (classification problems).
"""

import warnings
import pandas as pd
import numpy as np
warnings.filterwarnings('ignore')


# ## PLOT: Total Metrics

def total_metrics(data: 'df', sobservation: str, sprediction: str):
    """
    Plot an error analysis overview for whole data.
    data -- df where is included the data to be validated.
    sobservation -- column name of real data.
    sprediction -- column name of predicted data.
    return -- {'accuracy':accuracy, 'recall_weighted':recall_weighted, 'precision_weighted':precision_weighted, 'f1_weighted': f1_weighted}
    """

    # copy data
    df = data[[sobservation, sprediction]].dropna()
    # collect classes
    lc_obs = sorted(list(df[sobservation].unique()))
    lc_frc = sorted(list(df[sprediction].unique()))
    # validate if there are the same classess
    lc_diff = list(set(lc_obs) - set(lc_frc))
    # filter
    if len(lc_diff) > 0:
        n1 = len(df)
        df = df[~df[sobservation].isin(lc_diff)]
        df = df[~df[sprediction].isin(lc_diff)]
        n2 = len(df)
    # validation of format
    if not df.dtypes.values[0] == np.dtype('O') or not df.dtypes.values[0] == str:
        df[sobservation] = df[sobservation].astype(np.dtype('O'))
    if not df.dtypes.values[1] == np.dtype('O') or not df.dtypes.values[1] == str:
        df[sprediction] = df[sprediction].astype(np.dtype('O'))
    # final list of classess
    lc = ['%i' % ic if type(ic) == float else str(ic) for ic in sorted(list(df[sobservation].unique()))]

    # classification report
    targets = np.vstack(df[sobservation].values)
    pred_classes = np.vstack(df[sprediction].values)
    results = classification_report(targets, pred_classes, target_names=lc)
    # accuracy
    aux = df[[sobservation, sprediction]].apply(lambda x: True if x[0] == x[1] else False, axis=1).values
    accuracy = len(aux[aux == True]) / (len(aux))
    del aux

    # display results
    print(results)
    print('accuracy           %.2f' % accuracy)

    # return essential metrics
    recall_weighted = recall_score(targets, pred_classes, average='weighted')
    precision_weighted = precision_score(targets, pred_classes, average='weighted')
    f1_weighted = f1_score(targets, pred_classes, average='weighted')
    return {'accuracy': accuracy, 'recall_weighted': recall_weighted, 'precision_weighted': precision_weighted, 'f1_weighted': f1_weighted}
