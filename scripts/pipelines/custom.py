# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-09-11 13:15:43
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-09-11 13:54:10

"""
Custom classes for scikit-learn pipelines.
"""

from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class TypeSelector(BaseEstimator, TransformerMixin):
    """
    Data columns selector by data type.
    dtype -- data type selector:
        float: np.float or 'float' or float
        integer: np.int or 'int' or int
        bool: np.bool or 'bool' or bool
        categorical: 'category'
        numerical: np.number
    """

    def __init__(self, dtype: 'data type'):
        self.dtype = dtype

    def fit(self, X: 'df', y: 'df'=None):
        return self

    def transform(self, X: 'df'):
        assert isinstance(X, pd.DataFrame)
        return X.select_dtypes(include=[self.dtype])


class StringIndexer(BaseEstimator, TransformerMixin):
    """
    Indexation of strings. Each different string will be indexed with an unique index.
    WARNING: it can work extremely slow if it is required to index too much strings.
    """

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        assert isinstance(X, pd.DataFrame)
        return X.apply(lambda s: s.cat.codes.replace(
            {-1: len(s.cat.categories)}
        ))


class ColumnSelector(object):
    """
    A feature selector for scikit-learn's Pipeline class that returns specified columns from a numpy array.
    cols -- list of the selected index columns.
    """

    def __init__(self, cols):
        self.cols = cols

    def transform(self, X, y=None):
        return X[:, self.cols]

    def fit(self, X, y=None):
        return self
