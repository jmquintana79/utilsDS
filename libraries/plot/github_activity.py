# @Author: juan
# @Date:   2018-12-13T12:49:20+09:00
# @Last modified by:   juan
# @Last modified time: 2018-12-13T12:54:13+09:00

## PLOT: GitHub activitie
def show(df:'df', slabel_x:str='', slabel_y:str='', stitle:str=''):
    """
    Plot chart similar than GitHub activity chart.
    df-- data to be plotted with these column names: "x", "y", "activity".
    slabel_x -- label to me printed on X-axis.
    slabel_y -- label to me printed on Y-axis.
    stitle -- title to be printed.
    """
    import matplotlib.pyplot as plt
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    # validation
    assert "x" in df.columns, 'It is required the column "x".'
    assert "y" in df.columns, 'It is required the column "y".'
    assert "activity" in df.columns, 'It is required the column "activity".'
    # reshape the data and plot it
    df2 = df.pivot(columns="x", index="y", values="activity")
    df2.fillna(0, inplace=True)
    # data collection
    IY, IX = np.mgrid[:df2.shape[0]+1, :df2.shape[1]+1]
    # chart
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.set_aspect("equal")
    divider = make_axes_locatable(ax)
    img = ax.pcolormesh(IX, IY, df2.values, cmap="Greens", edgecolor="w", vmin=(0.75)*np.min(df2.values), vmax=np.max(df2.values))
    plt.xlim(0, df2.shape[1])
    plt.title(stitle)
    plt.xlabel(slabel_x)
    plt.ylabel(slabel_y)
    cax = divider.append_axes("right", size="2.5%", pad=0.05)
    fig.colorbar(img, cax=cax)
    plt.show()

if __name__=="__main__":
    import numpy as np
    import pandas as pd

    # some random data
    N = 100
    np.random.seed(0)
    weekday = np.random.randint(0, 7, N)
    week = np.random.randint(0, 40, N)
    activity = np.random.randint(0, 100, N)
    # preparation
    df = pd.DataFrame({"weekday":weekday, "week":week, "activity":activity})
    df.drop_duplicates(subset=["weekday", "week"], inplace=True)
    df.rename(columns={'weekday':'y', 'week':'x'},inplace = True)
    # launching example
    show(df, 'weeks', 'weekdays', 'Contributions')
