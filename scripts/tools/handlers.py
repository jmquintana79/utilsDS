# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-08-06 16:47:54
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-08-07 11:30:45

import pandas as pd


# READER
def reader(path: str, sep: str=",", lindex: list=[], starget: str="", ddt: dict=dict())->tuple:
    """
    Reader of csv files.
    path -- path of input file.
    sep -- separator (default ',').
    lindex -- list of column to be indexed (default []).
    starget -- column name of the target variable (default '').
    ddt -- dictionary to format datetime columns. ( format ddt ={
                                                                'lcol':[LIST OF COLUMNS],
                                                                'sformat:"DATETIME FORMAT STRING"} )
    return (df data, dictionary with columns information ('ly','lx','lx_float','lx_int','lx_cat'))
    """
    try:
        # read data
        dfdata = pd.read_csv(path, sep=sep)
        lcol = list(dfdata.columns)
        # if there are a datetime column
        if len(ddt) > 0:
            for isdt in ddt['lcol']:
                dfdata[isdt] = pd.to_datetime(
                    dfdata[isdt], format=ddt['sformat'])
                lcol.remove(isdt)
        # if there are an index
        if len(lindex) > 0:
            dfdata = dfdata.set_index(lindex)
            for isindex in lindex:
                lcol.remove(isindex)
        # if there are a target
        if len(starget) > 0:
            dfdata.rename(columns={starget: 'y'}, inplace=True)
            lcol.remove(starget)
            starget = 'y'

        # list of columns per type
        lcol_float = list(dfdata[lcol].select_dtypes(
            include=['float64']).columns.values)
        lcol_int = list(dfdata[lcol].select_dtypes(
            include=['int64']).columns.values)
        lcol_cat = list(dfdata[lcol].select_dtypes(
            include=['object']).columns.values)

        # store column names
        dfcolname = {
            'ly': [starget],
            'lx': lcol,
            'lx_float': lcol_float,
            'lx_int': lcol_int,
            'lx_cat': lcol_cat
        }
    except Exception as e:
        print('[error] there are any problem reading the input file "%s"' % path)
        print(str(e))
        return (pd.DataFrame(), dict())

    # return
    return (dfdata, dfcolname)


# MAIN
if __name__ == '__main__':
    import os
    import sys
    sys.path.append('../../arguments/')
    from _arguments import *

    # read
    path_input = os.path.join(folder_data_raw, 'load_iris.csv')
    dfdata, dcolumns = reader(path_input)
    print('\ndata:\n', dfdata.head())
    print('\ncolumns:\n', dcolumns)

    # end
    quit('\ndone!')
