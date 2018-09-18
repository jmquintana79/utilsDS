# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-09-18 09:24:26
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-09-18 11:29:23


"""
DATASET Kaggle Titanic.
"""
import numpy as np
import sys
sys.path.append('../../../')
from tools.reader import get_dcol, csv2df
import click

FILE_TRAIN = 'train.csv.gz'
FILE_TEST = 'test.csv.gz'


def train()->tuple:
    """
    Load training dataset.
    return -- tuple(dataframe data, dictionary columns)
    """
    # header
    click.secho('Load data..', fg='green')
    # read data
    df, dcol = csv2df(FILE_TRAIN, ltarget=['Survived'], lindex=['PassengerId'])
    # return
    return (df, dcol)


def test()->tuple:
    """
    Load test dataset.
    return -- tuple(dataframe data, dictionary columns)
    """
    # header
    click.secho('Load data..', fg='green')
    # read data
    df, dcol = csv2df(FILE_TEST, ltarget=[], lindex=['PassengerId'])
    # return
    return (df, dcol)


if __name__ == '__main__':
    # load training data
    dftrain, dcol_train = train()
    print('Training data:')
    print(dcol_train)
    # load test data
    dftest, dcol_test = test()
    print('Test data:')
    print(dcol_test)
