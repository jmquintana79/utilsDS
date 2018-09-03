# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-09-03 15:51:17
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-09-03 15:54:32

"""
Load data for any experiment.
"""
import numpy as np
import pandas as pd
from sklearn import datasets


def data():
    # Load Diabetes datasets
    diabetes = datasets.load_diabetes()
    X = diabetes.data
    y = diabetes.target

    # Create pandas DataFrame for sklearn ElasticNet linear_model
    Y = np.array([y]).transpose()
    d = np.concatenate((X, Y), axis=1)
    cols = diabetes.feature_names + ['progression']
    data = pd.DataFrame(d, columns=cols)

    # return
    return data


if __name__ == '__main__':
    dfdata = data()
    print(dfdata.head())
