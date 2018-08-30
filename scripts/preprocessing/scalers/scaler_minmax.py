# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-08-30 16:10:29
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-08-30 17:47:08

"""
Min-Max scaler based on 'sklearn.preprocessing.MinMaxScaler' with extra save/load functionality.
"""

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

    def fit(self, data: 'array'):
        """
        Fit the scaler.
        data -- array of data.
        """
        try:
            self.scaler.fit(data)
            self.isfitted = True
        except Exception as e:
            print('[error] it was not possible fit the scaler.')
            print(str(e))

    def transform(self, data: 'array') -> 'array':
        """
        Transform.
        data -- array of data.
        return -- scaled data array.
        """
        try:
            if self.isfitted:
                return self.scaler.transform(data)
            else:
                print('[warning] the scaler was not fitted yet.')
                return None
        except Exception as e:
            print('[error] the data could not be scaled.')
            print(str(e))
            return None

    def fit_transform(self, data: 'array') -> 'array':
        """
        Fit and ransform.
        data -- data array.
        return -- scaled data array.
        """
        try:
            # fit
            self.scaler.fit(data)
            self.isfitted = True
            # transform
            return self.scaler.transform(data)
        except Exception as e:
            print('[error] the data could not be fitted or scaled.')
            print(str(e))
            return None

    def inverse_transform(self, data: 'array') -> 'array':
        """
        Inverse transformation.
        data -- scaled data array.
        return -- inverted data array.
        """
        try:
            if self.isfitted:
                return self.scaler.inverse_transform(data)
            else:
                print('[warning] the scaler was not fitted yet.')
                return None
        except Exception as e:
            print('[error] there are any problem in the inverse transformation.')
            print(str(e))
            return None

    def save(self, path: str):
        """
        Save a scaler.
        path -- path of the output file.
        """
        import pickle

        try:
            if self.isfitted:
                # validate path
                if path[-3:] != '.sav':
                    path = '%s.sav' % path
                # save
                pickle.dump(self.scaler, open(path, 'wb'))
                print('[info] the scaler was saved in "%s".' % path)
            else:
                print('[warning] it is not possible save the scaler because it was not fitted yet.')
        except Exception as e:
            print('[error] there are any problem in the inverse transformation.')
            print(str(e))
            return None

    def load(self, path: str):
        """
        Load a scaler.
        path -- path of the input file.
        """
        import pickle
        from os.path import split

        try:
            if self.isfitted:
                # validate path
                if path[-3:] != '.sav':
                    path = '%s.sav' % path
                # save
                self.scaler = pickle.load(open(path, 'rb'))
                print('[info] the scaler "%s" was loaded.' % split(path)[-1])
            else:
                print('[warning] it is not possible save the scaler because it was not fitted yet.')
        except Exception as e:
            print('[error] there are any problem in the inverse transformation.')
            print(str(e))
            return None


if __name__ == '__main__':
    import sys
    import numpy as np

    # load dataset
    sys.path.append('../../')
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
    scaler.load(path)
