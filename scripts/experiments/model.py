# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-09-03 16:58:42
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-09-03 17:13:51

"""
MODEL SCRIPT.
"""
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet


def launcher(data, alpha, l1_ratio):
    # # data preparation

    # split the data into training and test sets. (0.75, 0.25) split.
    train, test = train_test_split(data)
    # collect data
    train_x = train.drop(["progression"], axis=1)
    test_x = test.drop(["progression"], axis=1)
    train_y = train[["progression"]]
    test_y = test[["progression"]]
    print('[info] Training data: x = (%s, %s)   y = (%s, %s)' % (train_x.shape[0], train_x.shape[1], train_y.shape[0], train_y.shape[1]))
    print('[info] Test data:     x = (%s, %s)   y = (%s, %s)' % (test_x.shape[0], test_x.shape[1], test_y.shape[0], test_y.shape[1]))

    # # model

    # Run ElasticNet
    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
    lr.fit(train_x, train_y)
    test_yhat = lr.predict(test_x)

    # return
    return (test_y, test_yhat, test_x.shape[1])
