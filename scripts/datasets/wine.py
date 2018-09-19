# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-09-18 09:24:26
# @Last Modified by:   jmquintana79
# @Last Modified time: 2018-09-18 20:04:14


"""
DATASET wine without target variable.
"""
import numpy as np
import sys
sys.path.append('../')
from tools.reader import get_dcol, csv2df
import click
import os

this_dir, this_filename = os.path.split(__file__)
FILE = 'data/dataset.wine.csv.gz'
PATH = os.path.join(this_dir, FILE)


def load()->tuple:
    """
    Load wine dataset (without target variable).
    return -- tuple(dataframe data, dictionary columns)
    """
    # header
    click.secho('Load data..', fg='green')
    # read data
    df, dcol = csv2df(PATH)
    # format
    df.Proline = df.Proline.astype(float)
    df.Magnesium = df.Magnesium.astype(float)
    df.Alcohol = df.Alcohol.astype(int)
    # update dcol
    dcol = get_dcol(df)
    # return
    return (df, dcol)


def save(path: str):
    # load dataset
    data, dcol = load()
    # store into a csv file
    try:
        data.to_csv(path, index=False)
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
    # save('dataset.wine.csv')
