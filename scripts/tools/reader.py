# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-08-06 16:47:54
# @Last Modified by:   jmquintana79
# @Last Modified time: 2018-09-28 23:08:41

from pandas import read_csv, to_datetime, DataFrame


class columns():
    """
    Dataframe column names container.
    """
    def __init__(self):
        self.all = list()
        self.x = list()
        self.y = list()
        self.float = list()
        self.int = list()
        self.cat = list()
        self.bool = list()
        self.index = dict()

    def get(self, dfdata:'df', target:list()=list()):
        """
        Collect and store column names of df. Furthermore, column names are
        classify per type.
        dfdata -- dataframe.
        target -- list of column names to be considered as target variables (default []).
        """
       # columns
        self.all = dfdata.columns.tolist()
        # collect and store column names
        self.y = target
        self.x = [icol for icol in self.all if not icol in target]
        self.float =  list(dfdata[self.all].select_dtypes(include=['float64']).columns.values)
        self.int = list(dfdata[self.all].select_dtypes(include=['int64']).columns.values)
        self.cat = list(dfdata[self.all].select_dtypes(include=['object', 'category']).columns.values)
        self.bool = list(dfdata[self.all].select_dtypes(include=['bool']).columns.values)
        # collect index
        class Index():
            def __init__(self):
                pass
        self.index = Index()
        for ii, icol in enumerate(self.all):
            setattr( self.index, icol, ii )

    def __str__(self):
        return "\ncolumns.x: %s\ncolumns.y: %s\ncolumns.float: %s\ncolumns.int: %s\ncolumns.cat: %s\ncolumns.bool: %s\n"%(self.x, self.y, self.float, self.int, self.cat, self.bool)





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
    return (df data, instance with columns information ('y','x','float','int','cat', 'bool', 'index'))
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
        col = columns()
        col.get(dfdata, ltarget)

        # give format to the dataframe
        for ic in col.cat:
            dfdata[ic] = dfdata[ic].astype('category')
        for ic in col.float:
            dfdata[ic] = dfdata[ic].astype('float')
        for ic in col.int:
            dfdata[ic] = dfdata[ic].astype('int')
        for ic in col.bool:
            dfdata[ic] = dfdata[ic].astype('bool')

    except Exception as e:
        print('[error] there are any problem reading the input file "%s"' % path)
        print(str(e))
        return (DataFrame(), dict())

    # return
    return (dfdata, col)


# MAIN
if __name__ == '__main__':
    import os

    # read: csv to df
    path_input = os.path.join('../datasets/kaggle/titanic', 'train.csv.gz')
    dfdata, columns = csv2df(path_input)
    print('\ndata:\n', dfdata.head())
    print('\ncolumns:\n', columns)
    print('\nselect a column by index:\n', dfdata.values[:,columns.index.Cabin][:5])

    # end
    quit('\ndone!')
