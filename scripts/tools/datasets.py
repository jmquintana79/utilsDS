# -*- coding: utf-8 -*-
# @Author: juan
# @Date:   2018-08-27 21:56:15
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-08-30 16:37:25

from pandas import DataFrame


class Data():
    def __init__(self):
        self.menu = ['boston', 'iris', 'diabetes']

    def load(self, sname: str):
        # cases
        if sname == 'boston':
            ## boston (regression)
            from sklearn.datasets import load_boston
            dataset = load_boston()
        elif sname == 'iris':
            ## iris (classification)
            from sklearn.datasets import load_iris
            dataset = load_iris()
        elif sname == 'diabetes':
            ## diabetes (regression)
            from sklearn.datasets import load_diabetes
            dataset = load_diabetes()
        else:
            print('[error] this dataset is not available.')
            return None

        # display shape
        print('[info] shape of loaded data: ', dataset.data.shape)

        # store data in df
        dfdata = DataFrame(dataset.data, columns=dataset.feature_names)
        dfdata['target'] = dataset.target
        lcol = list(dfdata.columns)

        # list of columns per type
        lcol_float = list(dfdata[lcol].select_dtypes(
            include=['float64']).columns.values)
        lcol_int = list(dfdata[lcol].select_dtypes(
            include=['int64']).columns.values)
        lcol_cat = list(dfdata[lcol].select_dtypes(
            include=['object']).columns.values)

        # store column names
        dcol = {
            'ly': ['target'],
            'lx': [icol for icol in lcol if not icol is 'target'],
            'lc_float': lcol_float,
            'lc_int': lcol_int,
            'lc_cat': lcol_cat
        }

        # return
        return (dfdata, dcol)


if __name__ == '__main__':
    # object
    dataset = Data()
    print('Available dataset: %s' % dataset.menu)
    # load dataset
    print('Load boston dataset:')
    data, dcol = dataset.load('boston')
    print(dcol)
    print(data.head())
