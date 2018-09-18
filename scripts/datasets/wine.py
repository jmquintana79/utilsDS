# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-09-18 09:24:26
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-09-18 11:49:59


"""
DATASET wine without target variable.
"""
import numpy as np
import sys
sys.path.append('../')
from tools.reader import get_dcol, csv2df
import click

FILE = 'data/dataset.wine.csv.gz'


def load()->tuple:
    """
    Load wine dataset (without target variable).
    return -- tuple(dataframe data, dictionary columns)
    """
    # header
    click.secho('Load data..', fg='green')
    # read data
    df, dcol = csv2df(FILE)
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
