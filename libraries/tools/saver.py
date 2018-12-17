# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-08-21 17:43:03
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-08-21 17:51:28

import timer


# save submission data into csv file
def df2csv_submition(df: 'df', filename: str='sub_{}.csv.gz'):
    """Saves the passed dataframe with index=False, and enables GZIP compression if a '.gz' extension is passed.
    If '{}' exists in the filename, this is replaced with the current time from mlcrate.time.now()
    Keyword arguments:
    df -- The pandas DataFrame of the submission
    filename -- The filename to save the submission to. Autodetects '.gz'
    """
    if '{}' in filename:
        filename = filename.format(timer.now())
    if filename.endswith('.gz'):
        compression = 'gzip'
    else:
        compression = None
    try:
        df.to_csv(filename, index=False, compression=compression)
        print('[success] the file "%s" was saved.' % filename)
    except Exception as e:
        print('[error-save_sub] there are any problem saving "%s"' % filename)
        print(str(e))


if __name__ == '__main__':
    from pandas import DataFrame
    # dataset to df
    from sklearn.datasets import load_boston
    boston = load_boston()
    dfboston = DataFrame(boston.data, columns=boston.feature_names)
    # save submition
    df2csv_submit(dfboston, 'data-boston_{}.csv.gz')
