"""

It’ll be served the app with:
```
panel serve app.py --autoreload
```
Now, open the app in your browser at **http://localhost:5006/app**.

"""

import os
import numpy as np
import pandas as pd
import panel as pn
import holoviews as hv
from datetime import datetime, date
import hvplot.pandas

## SETTINGS
FOLDER_DATA= (
    "/Users/juan/Workspace/data/datasets/dashboards"
)

## DEPLOYING THE DASHBOARD

# initializate
material = pn.template.MaterialTemplate(
    site="Panel",
    title="Prueba App",
)

# read index
dfi = pd.read_csv(os.path.join(FOLDER_DATA, 'index.csv'))
# index dict creation
d_index = dict()
for ifather in dfi["father"].unique():
    d_index[ifather] = dfi[dfi.father == ifather]["son"].tolist()

# folders selection
folders_selection_widget = pn.widgets.NestedSelect(
    options=d_index, levels=["Father", "Sons"],
)

# plot
@pn.depends(folders_selection = folders_selection_widget, watch = False)
def plot(folders_selection):
    # buidl path
    folder = os.path.join(FOLDER_DATA, folders_selection["Father"], folders_selection["Sons"])
    # files to be read
    files = os.listdir(folder)

    print(folders_selection)
    print(folder)
    print(files)


# add dashboard elements
material.sidebar.append(folders_selection_widget)
material.main.append(plot)
# deploy
#material.show()
material.servable();
