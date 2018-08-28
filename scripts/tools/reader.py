# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-08-06 16:47:54
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-08-28 11:36:42

from pandas import read_csv, to_datetime, DataFrame


# get dictionary of columns by type
def get_dcol(dfdata: 'df', ltarget: list=list())->dict:
    # columns
    lcol = dfdata.columns.tolist()
    # list of columns per type
    lcol_float = list(dfdata[lcol].select_dtypes(
        include=['float64']).columns.values)
    lcol_int = list(dfdata[lcol].select_dtypes(
        include=['int64']).columns.values)
    lcol_cat = list(dfdata[lcol].select_dtypes(
        include=['object']).columns.values)

    # store column names
    dfcolname = {
        'ly': ltarget,
        'lx': [icol for icol in lcol if not icol in ltarget],
        'lc_float': lcol_float,
        'lc_int': lcol_int,
        'lc_cat': lcol_cat
    }
    # return
    return dfcolname


# READER: csv file to dataframe
def csv2df(path: str, lindex: list=[], ltarget: list=list(), ddt: dict=dict(), **kwargs)->tuple:
    """
    Reader of csv files and store into a dataframe.
    path -- path of input file.
    lindex -- list of column to be indexed (default []).
    ltarget -- list of column names of the target variables (default []).
    ddt -- dictionary to format datetime columns. ( format ddt ={
                                                                'lcol':[LIST OF COLUMNS],
                                                                'sformat:"DATETIME FORMAT STRING"} )
    **kwargs -- dict other arguments: sep, usecols
    return (df data, dictionary with columns information ('ly','lx','lx_float','lx_int','lx_cat'))
    """

    # usecols
    if not 'usecols' in kwargs:
        kwargs['usecols'] = None
    if not 'sep' in kwargs:
        kwargs['sep'] = ','

    try:
        # read data
        dfdata = read_csv(path, sep=kwargs['sep'], usecols=kwargs['usecols'])

        # if there are a target
        if len(ltarget) == 1 and len(ltarget[0]) > 0:
            dfdata.rename(columns={ltarget[0]: 'y'}, inplace=True)
            ltarget = ['y']

        # if there are a datetime column
        if len(ddt) > 0:
            for isdt in ddt['lcol']:
                dfdata[isdt] = to_datetime(
                    dfdata[isdt], format=ddt['sformat'])

        # if there are an index
        if len(lindex) > 0:
            dfdata = dfdata.set_index(lindex)

        # collect list of columns per type
        dfcolname = get_dcol(dfdata, ltarget)

    except Exception as e:
        print('[error] there are any problem reading the input file "%s"' % path)
        print(str(e))
        return (DataFrame(), dict())

    # return
    return (dfdata, dfcolname)


# MAIN
if __name__ == '__main__':
    import os
    # read: csv to df
    path_input = os.path.join('../../datasets/', 'dataset.weather.csv')
    dfdata, dcolumns = csv2df(path_input)
    print('\ndata:\n', dfdata.head())
    print('\ncolumns:\n', dcolumns)

    # end
    quit('\ndone!')
