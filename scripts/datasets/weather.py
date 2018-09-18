# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-09-18 09:24:26
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-09-18 11:50:17


"""
DATASET weather without target variable.
"""
import numpy as np
import sys
sys.path.append('../')
from tools.reader import csv2df
import click

FILE = 'data/dataset.weather.csv.gz'


def load()->tuple:
    """
    Load weather dataset (without target variable).
    return -- tuple(dataframe data, dictionary columns)
    """
    # header
    click.secho('Load data..', fg='green')
    # read data
    ddt = {'lcol': ['datetime'], 'sformat': '%Y-%m-%d %H:%M:%S'}
    df, dcol = csv2df(FILE, lindex=['datetime'], ddt=ddt)
    # return
    return (df, dcol)


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
    data, dcol = load()
    # save data
    # save('dataset.weather.csv')
