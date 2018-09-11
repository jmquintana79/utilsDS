# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-09-11 13:38:00
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-09-11 14:26:55

"""
Basic scikit-learn pipeline to prepare the features according
type of each column to be used in a ML algorithm:
 - boolean: no transformation.
 - numerical (int, float): standarization.
 - categorical: Hot Encoder (get dummies).
"""

from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from pipelines.custom import *
import numpy as np

# for all types of data
pipe_types = Pipeline([
    ('features', FeatureUnion(n_jobs=-1, transformer_list=[
        # Part 1
        ('boolean', Pipeline([
            ('selector', TypeSelector('bool')),
        ])),  # booleans close

        ('numericals', Pipeline([
            ('selector', TypeSelector(np.number)),
            ('scaler', StandardScaler()),
        ])),  # numericals close

        # Part 2
        ('categoricals', Pipeline([
            ('selector', TypeSelector('category')),
            ('labeler', StringIndexer()),
            ('encoder', OneHotEncoder(handle_unknown='ignore')),
        ]))  # categoricals close
    ])),  # features close
])  # pipeline close


# only for numerical and boolean data
pipe_numerical = Pipeline([
    ('features', FeatureUnion(n_jobs=-1, transformer_list=[
        # Part 1
        ('boolean', Pipeline([
            ('selector', TypeSelector('bool')),
        ])),  # booleans close

        ('numericals', Pipeline([
            ('selector', TypeSelector(np.number)),
            ('scaler', StandardScaler()),
        ])),  # numericals close
    ])),  # features close
])  # pipeline close
