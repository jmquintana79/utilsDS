# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2024-11-09 18:30:28
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2024-11-09 20:42:08
import numpy as np
import pandas as pd
import panel as pn
import holoviews as hv
from holoviews import opts

# Configurar las extensiones
pn.extension('bokeh')
hv.extension('bokeh')

# Generar datos de ejemplo
np.random.seed(0)
date_rng = pd.date_range(start='2022-01-01', end='2022-01-30', freq='h')
data = pd.DataFrame(date_rng, columns=['date'])
data['value'] = np.random.randn(len(date_rng))
data['value2'] = np.random.randn(len(date_rng))
data['scatter_x'] = np.random.randn(len(date_rng))
data['scatter_y'] = np.random.randn(len(date_rng))

# Convertir a un formato de Holoviews con los datos de ejemplo
ts1 = hv.Curve((data['date'], data['value']), 'date', 'value').opts(title="Time Series 1", width=1600, height=300)
ts2 = hv.Curve((data['date'], data['value2']), 'date', 'value2').opts(title="Time Series 2", width=1600, height=300)
scatter = hv.Scatter((data['scatter_x'], data['scatter_y']), 'scatter_x', 'scatter_y').opts(title="Scatter Plot", width=1600, height=600)

# Configurar ligadura de selección entre gráficos
linked_ts1 = ts1.opts(opts.Curve(tools=['box_select', 'lasso_select'], active_tools=['box_select']))
linked_ts2 = ts2.opts(opts.Curve(tools=['box_select', 'lasso_select'], active_tools=['box_select']))
#linked_scatter = scatter.opts(opts.Scatter(tools=['box_select', 'lasso_select'], active_tools=['box_select']))

# Crear el layout del dashboard con Panel
dashboard = pn.Column(
    pn.pane.Markdown("## Dashboard Interactivo"),
    scatter,
    linked_ts1,
    linked_ts2
)

# Guardar como HTML
dashboard.save('dashboard_interactivo.html', embed=True)
