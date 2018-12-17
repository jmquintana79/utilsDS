# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-09-18 09:24:26
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-10-04 15:43:13


"""
DATASET weather without target variable.
"""
import numpy as np
import sys
sys.path.append('../')
from tools.reader import csv2df
import click
import os

this_dir, this_filename = os.path.split(__file__)
FILE = 'data/dataset.weather.csv.gz'
PATH = os.path.join(this_dir, FILE)


def load()->tuple:
    """
    Load weather dataset (without target variable).
    return -- tuple(dataframe data, dictionary columns)
    """
    # header
    click.secho('Load data..', fg='green')
    # read data
    ddt = {'lcol': ['datetime'], 'sformat': '%Y-%m-%d %H:%M:%S'}
    df, col = csv2df(PATH, lindex=['datetime'], ddt=ddt)
    # return
    return (df, col)


def save(path: str):
    # load dataset
    data, dcol = load()
    # store into a csv file
    try:
        data.to_csv(path, index=True)
        # screen
        click.secho('It was saved "%s" successfully.' % click.format_filename(path, shorten=True), fg='green')
    except Exception as e:
        click.secho('It could not be saved "%s" successfully.' % click.format_filename(path, shorten=True), fg='red')
        click.echo(str(e))

    # return
    return None


if __name__ == '__main__':
    # load data
    data, col = load()
    # print(col.all)
    # save data
    # save('dataset.weather.csv')
