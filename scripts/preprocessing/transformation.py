# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-09-11 13:09:47
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-09-11 14:29:28

"""
Data transfromation of X data just before to use a ML algorithm.
"""
import sys
sys.path.append('../')
from pipelines import transformer
import click


def launch_types(df: 'dataframe')->'array':
    """
    Launch a pre-processing Pipeline with numerical and categorical variables.
    df -- data to be transformed.
    """
    # validate if there are NaN values.
    if df.isnull().sum().sum() > 0:
        click.secho('[error] the dataframe to be transformated contains NaN values.', fg='red', bold=True)
        print(df.isnull().sum())
        quit('Aborted!')

    # fit, transform and return
    return transformer.pipe_types.fit_transform(df).toarray()


def launch_numerical(df: 'dataframe')->'array':
    """
    Launch a pre-processing Pipeline with only numerical variables.
    df -- data to be transformed.
    """
    # validate if there are NaN values.
    if df.isnull().sum().sum() > 0:
        click.secho('[error] the dataframe to be transformated contains NaN values.', fg='red', bold=True)
        print(df.isnull().sum())
        quit('Aborted!')

    # fit, transform and return
    return transformer.pipe_numerical.fit_transform(df)


if __name__ == '__main__':
    from tools import reader
    # read data
    data, dcol = reader.csv2df('../../datasets/dataset.weather.csv', lindex=['datetime'])
    # get a sample
    dfX = data[dcol['lc_float'][:1] + dcol['lc_cat'][:1]]
    # transformation
    X = launch_types(dfX.dropna().head())
    print(X)
