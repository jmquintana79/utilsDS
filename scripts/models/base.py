# -*- coding: utf-8 -*-
# @Author: jmquintana79
# @Date:   2018-08-30 23:54:47
# @Last Modified by:   jmquintana79
# @Last Modified time: 2018-08-31 00:54:57

import numpy as np
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.model_selection import cross_val_predict
from metrics import metrics_regression



class Base():
    def __init__(self,estimator):
        self.estimator = estimator

    def fit(self, X, y):
         # check that X and y have correct shape
         X, y = check_X_y(X, y)
         # set as attributes
         self.X_ = X
         self.y_ = y

    def predict(self):
        # check is fit had been called
        check_is_fitted(self, ['X_', 'y_'])
        # input validation
        X = check_array(X)

    def scores(self):
        pass

    def tuning1(self):
        pass

    def tuning2(self):
        pass

    def get_params(self, deep=True):
        # suppose this estimator has parameters "alpha" and "recursive"
        #return {"alpha": self.alpha, "recursive": self.recursive}
        pass

    def set_params(self, **parameters):
        for parameter, value in parameters.items():
            setattr(self, parameter, value)
        return self


class Regressor(Base):
    def __init__(self):
        pass


class Classificator(Base):
    def __init__(self):
        pass


if __name__ == '__main__':
    pass
