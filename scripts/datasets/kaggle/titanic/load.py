# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-09-18 09:24:26
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-10-04 15:44:51


"""
DATASET Kaggle Titanic.
"""
import numpy as np
import sys
sys.path.append('../../../')
from tools.reader import columns, csv2df
import click
import os

FILE_TRAIN = 'train.csv.gz'
FILE_TEST = 'test.csv.gz'
this_dir, this_filename = os.path.split(__file__)
PATH_TRAIN = os.path.join(this_dir, FILE_TRAIN)
PATH_TEST = os.path.join(this_dir, FILE_TEST)


def train()->tuple:
    """
    Load training dataset.
    return -- tuple(dataframe data, dictionary columns)
    """
    # header
    click.secho('Load data..', fg='green')
    # read data
    df, col = csv2df(PATH_TRAIN, ltarget=['Survived'], lindex=['PassengerId'])
    # return
    return (df, col)


def test()->tuple:
    """
    Load test dataset.
    return -- tuple(dataframe data, dictionary columns)
    """
    # header
    click.secho('Load data..', fg='green')
    # read data
    df, col = csv2df(PATH_TEST, ltarget=[], lindex=['PassengerId'])
    # return
    return (df, col)


if __name__ == '__main__':
    # load training data
    dftrain, col_train = train()
    print('Training data:')
    print(col_train.all)
    # load test data
    dftest, col_test = test()
    print('Test data:')
    print(col_test.all)
