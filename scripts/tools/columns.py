# -*- coding: utf-8 -*-
# @Author: juan
# @Date:   2018-08-27 23:05:18
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-08-28 10:15:25

from pandas import cut, isnull


# numerical column to categorical
def num2cal(dfdata: 'df', colname: str, lbins: list, llabels: list)->'df':
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
        dfdata['c%s' % colname] = cut(dfdata[colname], bins=lbins, include_lowest=True, labels=llabels).values
    except Exception as e:
        print(str(e))
        return None
    # return
    return dfdata


# inpute missing values according the median of another reference column.
def miss2median(df: 'df', scol: str, scolref: str)->'df':
    """
    Inpute missing values according the median of another reference column.
    df -- dataframe with missing values in any column.
    scol -- column of df with missing values.
    scolref -- column of df to be used as a reference to calculate the groupby().median().
    return -- dataframe with inputed missing values.
    """
    # looking for the scolref values with missing values in the target variable
    ldtmiss = df[isnull(df[scol])][scolref].tolist()
    # collect all data with these values and groupby according to each date calculating the median of the target variable
    linputed = df[df[scolref].isin(ldtmiss)][[scolref, scol]].groupby(scolref).median()[[scol]].values
    # collect df indexes of rows with missing values in the target variable
    lindex = df[isnull(df[scol])].index.tolist()
    # inpute calculated values
    ni = df[[scol]].isnull().sum().values[0]
    for i, ii in enumerate(lindex):
        df.set_value(ii, scol, linputed[i])
    nf = df[[scol]].isnull().sum().values[0]
    print('[info] it was inputed %s values of the "%s" column.' % (ni-nf, scol))
    # return
    return df


if __name__ == '__main__':
    # dataset
    import datasets
    dset = datasets.Data()
    dfdata, dcol = dset.load('boston')
    # set bins
    lbins = [5., 22.5, 50.]
    # set labels
    llabels = ['low', 'high']
    # categorize target column
    dfdata = num2cal(dfdata, 'target', lbins, llabels)
    print(dfdata[['target', 'ctarget']].head())
