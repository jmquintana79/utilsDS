# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2024-11-09 15:48:02
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2024-11-10 00:04:52
"""
panel serve app.py --autoreload
"""

import os
import hvplot.pandas
import numpy as np
import pandas as pd
import panel as pn
from datetime import datetime, date
from bokeh.resources import INLINE

pn.extension(design="material", sizing_mode="stretch_width")

""" ARGUMENTS """

PRIMARY_COLOR = "#0072B5"
SECONDARY_COLOR = "#B54300"
PATH_DATA= (
    "/Users/juan/Workspace/data/datasets/dashboards/DAILY/DAILY-T1/Wind Time Series Dataset(hourly).csv"
)
min_date = date(2014, 10, 1)
max_date = date(2016, 1, 1)



""" FUNCTIONS """

def load_data():
    if os.path.exists(PATH_DATA):
        return pd.read_csv(PATH_DATA).dropna()
    else:
        raise ValueError("Input file does not exist.")

def date_to_datetime(dt):
    return datetime(dt.year, dt.month, dt.day, 0, 0, 0)

def transform_data(data):
    data.set_index("Time", inplace = True)
    data.WindSpeed = data.WindSpeed.astype(float) 
    data.Power = data.Power.astype(float) 
    data.index = pd.to_datetime(data.index)
    return data

def get_plot(date_range, variable ="Power"):
    dti = date_to_datetime(date_range[0])   
    dtf = date_to_datetime(date_range[1])
    data_filtered = data[(data.index>=dti) & (data.index<=dtf)]
    return data_filtered[variable].hvplot(
        height=300, legend=False, color=PRIMARY_COLOR
    )# * highlight.hvplot.scatter(color=SECONDARY_COLOR, padding=0.1, legend=False)

def get_scatter(date_range):
    dti = date_to_datetime(date_range[0])   
    dtf = date_to_datetime(date_range[1])
    data_filtered = data[(data.index>=dti) & (data.index<=dtf)]
    return data.hvplot.scatter(x='WindSpeed', y='Power',
        color=PRIMARY_COLOR, padding=0.1, legend=False, alpha = .5, height=800
        )* data_filtered.hvplot.scatter(x='WindSpeed', y='Power', color=SECONDARY_COLOR, padding=0.1, legend=False)


""" WIDGETS """

date_range_slider = pn.widgets.DateRangeSlider(
    name='Date Range Slider',
    start=min_date, end=date(2016, 1, 1),
    value=(min_date, date(2016, 1, 1)),
    step=2
)

""" DASHBOARD """

data = load_data()
data = transform_data(data)

bound_plot_1 = pn.bind(
    get_plot, date_range = date_range_slider, variable="WindSpeed"
)
bound_plot_2 = pn.bind(
    get_plot, date_range = date_range_slider,variable="Power"
)
bound_plot_3 = pn.bind(
    get_scatter, date_range = date_range_slider
)

#content = pn.Column(date_range_slider, bound_plot_3, bound_plot_1, bound_plot_2)

template = pn.template.MaterialTemplate(    
    site="Panel",
    title="Prueba App",
    main=[date_range_slider, bound_plot_3, bound_plot_1, bound_plot_2],
)

#template.show()
template.save("test.html", resources=INLINE) # pip install panel==1.3.8


