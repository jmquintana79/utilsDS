# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-08-21 17:59:25
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-08-21 18:11:14

"""
Data model based on a Numpy array with extra funcionalities:
- Attached column names.
- Possible data selection by column or columns.
"""

import numpy as np

# basic numpy array with columns selector
class Array:
    """
    Basic numpy array with columns selector.

    Attributes:
    data -- array of X data.
    colums -- column names.
    ncols -- number of columns.
    nrows -- number of rows.
    """

    # constructor
    def __init__(self, array: 'np array', columns: list):
      """
      Array constructor.
      array -- array of X data.
      columns -- column names.
      """
      # validation
      assert type(array) == np.ndarray, "The data is not a numpy array."
      assert type(columns) == list, "The columns list not match with the data shape."
      assert array.shape[1] == len(columns), "The columns list not match with the data shape."
      # set attributes
      self.data = array
      self.col = columns
      # calculate number of rows and x columns
      self.nrow = self.data.shape[0]
      self.ncol = self.data.shape[1]

    # columns selector
    def sel(self, query: 'string or list of strings'):
      """
      Data column selector
      """
      if type(query) == str or type(query) == np.str_:
          return self.data[:, self.col.index(query)]
      elif type(query) == list:
          if len(query) == 0:
              return self.data
          elif len(query) == 1:
              return self.data[:, self.col.index(query[0])]
          else:
              return self.data[:, [self.col.index(iq) for iq in query]]
      else:
          return None

    # custom display
    def __repr__(self):
      return "<model.Array nrow:%s ncol:%s>" % (self.nrow, self.ncol)

    def __str__(self):
      return "model.Array: nrow=%s ncol=%s" % (self.nrow, self.ncol)


if __name__ == '__main__':
  # dataset
  from sklearn.datasets import load_boston
  boston = load_boston()
  # create object
  data = Array(boston.data, list(boston.feature_names))
  print(data)
  print('model.Array.col: %s'%data.col)
  print('model.Array.sel[%s]: %s'%(data.col[0], data.sel(data.col[0]).shape))
