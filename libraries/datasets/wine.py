# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-09-18 09:24:26
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-10-04 15:43:58


"""
DATASET wine without target variable.
"""
import numpy as np
import sys
sys.path.append('../')
from tools.reader import columns, csv2df
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
    col = columns()
    col.get(df)
    # return
    return (df, col)


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
    data, col = load()
    # print(col.all)
    # save data
    # save('dataset.wine.csv')
