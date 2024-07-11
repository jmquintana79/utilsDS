"""
https://discourse.holoviz.org/t/tips-for-saving-interactive-plots-as-html/175/2
> python app.py
"""
import holoviews as hv
import numpy as np
import panel as pn
import bokeh
from bokeh.resources import INLINE

hv.extension('bokeh') 

def sine_curve(phase, freq, elevation):
    xvals = [0.1* i for i in range(100)]
    yvals = [np.sin(phase+freq*x) + elevation for x in xvals]
    data = {'xvals': xvals, 'yvals': yvals}
    return hv.Points(data, kdims=['xvals','yvals'])

frequencies = [0.5+i*0.25 for i in range(5)] 
phases      = [i*np.pi/2 for i in range(5)]
elevations  = [i*0.1 for i in range(5)]
curve_dict = {(p,f,v): sine_curve(p,f,v) for p in phases for f in frequencies for v in elevations}
hmap = hv.HoloMap(curve_dict, kdims=['phase', 'frequency', 'elevation']).opts(height=500,width=500)

panel_object = pn.pane.HoloViews(hmap)
pn.pane.HoloViews(hmap).save('test', embed=True, resources=INLINE)