# -*- coding: utf-8 -*-
# @Author: juan
# @Date:   2018-08-27 23:05:18
# @Last Modified by:   juan
# @Last Modified time: 2018-08-27 23:45:50

from pandas import cut

## numerical column to categorical
def num2cal(dfdata:'df', colname:str, lbins:list, llabels: list)->'df':
    """
    Numerical column to categorical in dataframe
    dfdata - pandas dataframe.
    ncolumn - name of column to be converted.
    lbins - list of bins limits to categorize.
    llabels - list of labels to name each category. If len(lbins)==n then len(labels) = n-1
    return - dfdata with new columns
    """
    # conversion
    try:
        dfdata['c%s'%colname] = cut(dfdata[colname], bins=lbins, include_lowest=True, labels=llabels).values
    except Exception as e:
        print(str(e))
        return None
    # return
    return dfdata

if __name__ == '__main__':
    # dataset
    import datasets
    dset = datasets.Data()
    dfdata, dcol = dset.load('boston')
    # set bins
    lbins = [5., 22.5, 50.]
    # set labels
    llabels = ['low','high']
    # categorize target column
    dfdata = num2cal(dfdata,'target',lbins,llabels)
    print(dfdata[['target','ctarget']].head())

