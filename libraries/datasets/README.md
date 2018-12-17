# datasets
This is a compilation of useful datasets.

### Available datasets:
- [Scikit Learn-Boston](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html).
- [Scikit Learn-Iris](http://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html).
- [Scikit Learn-Diabetes](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes).

- My dataset: **Solar**.
    - Meteorological and solar energy data. The meteorological are predicted values (between 0 to 23 hours ahead) and the solar energy is real data.
    - Columns description:
     - dt: datetime.
     - hforecast: step ahead of weather predictions.
     - VGRD267: v component of wind (m/s).
     - UGRD267: u component of wind (m/s).
     - HWS267: module of wind speed (m/s).
     - LCDC267: low level cloud cover(percent).
     - MCDC267: medium level cloud cover (percent).
     - HCDC267: high level cloud cover (percent).
     - TCDC267: total cloud cover (percent).
     - cLCDC267: low level cloud conver (oktas).
     - cMCDC267: medium level cloud cover (oktas).
     - cHCDC267: high level cloud cover (oktas).
     - cTCDC267: total cloud cover (oktas).
     - PRES267: pressure local surface (pascals).
     - RH267: relative humidity (percent).
     - TMP267: temperature (kelvin degrees).
     - APCP267: 1h-accumulated precipitation (mm).
     - cAPCP267: categorized (ordinal) 1h-accumulated precipitation (labels= 'no rain', 'soft rain', 'rain').
     - logAPCP267: log(x+1) of the previous variable.
     - year: year.
     - month: month of year.
     - doy: day of year.
     - hour: hour of day.
     - y: solar energy production (kwh).
     - cy: solar energy formated as categorical (ordinal) variable (5 labels).
     - DSWRF267: downward horizontal irradiance (W/m2)
     - diffAPCP267: differences of precipitation between each value and the previous one (mm).
     - diffDSWRF267: differences of downward horizontal irradiance between each value and the previous one (W/m2).

- My dataset: **Weather**.
     - One year of weather variables without a target variable.

- [Kaggle-Titanic](https://www.kaggle.com/c/titanic/data).

- [Wine dataset](https://archive.ics.uci.edu/ml/datasets/Wine).
