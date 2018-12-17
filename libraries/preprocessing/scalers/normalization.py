# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-08-30 16:10:29
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-08-31 18:17:17

"""
Min-Max scaler based on 'sklearn.preprocessing.MinMaxScaler' with extra save/load functionality.
"""
import sys
sys.path.append('../../')
from backend.decorators import valida
from sklearn.preprocessing import MinMaxScaler


class Scaler():
    def __init__(self, feature_range: tuple=(0, 1), copy: bool=True):
        """
        Initialize the object
        feature_range -- tuple of min-max range to scale the data (default (0,1)).
        copy -- avoid or not a copy (default True).
        """
        self.scaler = MinMaxScaler(feature_range=feature_range, copy=copy)
        self.isfitted = False
        self.parameters = dict()

    @valida
    def fit(self, data: 'array'):
        """
        Fit the scaler.
        data -- array of data.
        """
        # fit
        self.scaler.fit(data)
        self.isfitted = True
        # fill parameters
        self.parameters['data_min'] = self.scaler.data_min_
        self.parameters['data_max'] = self.scaler.data_max_
        self.parameters['scale'] = self.scaler.scale_

    @valida
    def transform(self, data: 'array') -> 'array':
        """
        Transform.
        data -- array of data.
        return -- scaled data array.
        """
        if self.isfitted:
            return self.scaler.transform(data)
        else:
            print('[warning] the scaler was not fitted yet.')
            return None

    @valida
    def fit_transform(self, data: 'array') -> 'array':
        """
        Fit and ransform.
        data -- data array.
        return -- scaled data array.
        """
        # fit
        self.scaler.fit(data)
        self.isfitted = True
        # fill parameters
        self.parameters['data_min'] = self.scaler.data_min_
        self.parameters['data_max'] = self.scaler.data_max_
        self.parameters['scale'] = self.scaler.scale_
        # transform
        return self.scaler.transform(data)

    @valida
    def inverse_transform(self, data: 'array') -> 'array':
        """
        Inverse transformation.
        data -- scaled data array.
        return -- inverted data array.
        """
        if self.isfitted:
            return self.scaler.inverse_transform(data)
        else:
            print('[warning] the scaler was not fitted yet.')
            return None

    @valida
    def save(self, path: str):
        """
        Save a scaler.
        path -- path of the output file.
        """
        import pickle
        if self.isfitted:
            # validate path
            if path[-3:] != '.sav':
                path = '%s.sav' % path
            # save
            pickle.dump(self.scaler, open(path, 'wb'))
            print('[info] the scaler was saved in "%s".' % path)
        else:
            print('[warning] it is not possible save the scaler because it was not fitted yet.')

    @valida
    def load(self, path: str):
        """
        Load a scaler.
        path -- path of the input file.
        """
        import pickle
        from os.path import split
        # validate path
        if path[-3:] != '.sav':
            path = '%s.sav' % path
        # load
        self.scaler = pickle.load(open(path, 'rb'))
        self.isfitted = True
        print('[info] the scaler "%s" was loaded.' % split(path)[-1])


if __name__ == '__main__':
    import numpy as np

    # load dataset
    from tools.datasets import *
    dataset = Data()
    dfdata, dcol = dataset.load('boston')
    data = dfdata[dcol['lx']].as_matrix()

    # create scaler object
    scaler = Scaler()
    print('[info] test:')
    # fit
    scaler.fit(data)
    print('[info] scaler was fitted: %s' % scaler.isfitted)
    # transform
    data_scaled = scaler.transform(data)
    print('\tdata shape: min = %.3f  max = %.3f' % (np.min(data[0, :]), np.max(data[0, :])))
    print('\tscaled data shape: min = %.3f  max = %.3f' % (np.min(data_scaled[0, :]), np.max(data_scaled[0, :])))

    # fit and transform
    scaler2 = Scaler()
    print('[info] test the fitting and transformation:')
    data_scaled2 = scaler2.fit_transform(data)
    print('\tdata shape: min = %.3f  max = %.3f' % (np.min(data[0, :]), np.max(data[0, :])))
    print('\tscaled data shape: min = %.3f  max = %.3f' % (np.min(data_scaled2[0, :]), np.max(data_scaled2[0, :])))

    # inverse transformation
    data_original = scaler.inverse_transform(data_scaled)
    print('[info] test the inverse transformation:')
    print('\tscaled data shape: min = %.3f  max = %.3f' % (np.min(data_scaled[0, :]), np.max(data_scaled[0, :])))
    print('\tdata shape: min = %.3f  max = %.3f' % (np.min(data_original[0, :]), np.max(data_original[0, :])))

    # save scaler
    from os.path import expanduser, join
    home = expanduser("~")
    path = join(home, 'Desktop', 'borrar')
    scaler.save(path)
    # load scaler
    scaler3 = Scaler()
    scaler3.load(path)
    print('[info] the loaded scaler is fitted: %s' % scaler3.isfitted)
    data_scaled3 = scaler3.transform(data)
    print('\tdata shape: min = %.3f  max = %.3f' % (np.min(data[0, :]), np.max(data[0, :])))
    print('\tscaled data shape: min = %.3f  max = %.3f' % (np.min(data_scaled3[0, :]), np.max(data_scaled3[0, :])))

    # parameters
    print('[info] parameters:')
    for k, v in scaler.parameters.items():
        print('\t-> "%s":' % k, v)
