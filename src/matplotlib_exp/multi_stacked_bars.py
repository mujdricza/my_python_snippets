"""
Examples for plotting multi-stacked bars from
https://stackoverflow.com/questions/47205918/plot-multiple-stacked-bar-in-the-same-figure

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def get_data():
    df = pd.DataFrame(
        dict(A=[1, 2, 3, 4], B=[2, 3, 4, 5], C=[3, 4, 5, 6], D=[4, 5, 6, 7])
    )
    return df


def stack_bars_v1(df: pd.DataFrame) -> None:
    """
    "Just keep in mind, the width value for one group must be positive, and negative for the second one. Use align by edge as well.
    You have to place the bar with the biggest values before the bar with the lowest values, and if you want the bars to appear stacked above one another rather than one in front of another, change df.B and df.D to df.B + df.A and df.D + df.C, respectively. If there's no apparent or consisting pattern, use the align by edge and width method with the one suggested by @piRSquared.
    Another alternative would be to access each value from a green bar and compare it to the corresponding value from the red bar, and plot accordingly (too much unnecessary work in this one)."
    """
    fig = plt.figure(figsize=(20, 10))

    ab_bar_list = [
        plt.bar([0, 1, 2, 3], df.B, align="edge", width=0.2),
        plt.bar([0, 1, 2, 3], df.A, align="edge", width=0.2),
    ]

    cd_bar_list = [
        plt.bar([0, 1, 2, 3], df.D, align="edge", width=-0.2),
        plt.bar([0, 1, 2, 3], df.C, align="edge", width=-0.2),
    ]

    # plt.plot(fig)
    plt.show()


def stack_bars_v2(df: pd.DataFrame) -> None:

    df.diff(axis=1).fillna(df).astype(df.dtypes).plot.bar(stacked=True)
    plt.show()


def stack_bars_v3(df: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)

    df.plot.bar(ax=axes[0])  # non-stacked variant
    df.diff(axis=1).fillna(df).astype(df.dtypes).plot.bar(ax=axes[1], stacked=True)

    plt.show()


def stack_bars_v4(df: pd.DataFrame) -> None:
    """
    there is in fact a direct way of stacking the bars via the bottom keyword
    (if you plot a horizontal barplot with plt.barh use left instead of bottom)!
    """
    df2 = df / 2

    f, ax = plt.subplots()
    ax.bar(df.index, df.A, align="edge", width=0.2)
    ax.bar(df.index, df.B, align="edge", width=0.2, bottom=df.A)
    ax.bar(df.index, df.C, align="edge", width=0.2, bottom=df.A + df.B)

    ax.bar(df2.index, df2.A, align="edge", width=-0.2)
    ax.bar(df2.index, df2.B, align="edge", width=-0.2, bottom=df2.A)
    ax.bar(df2.index, df2.C, align="edge", width=-0.2, bottom=df2.A + df2.B)

    plt.show()


def stack_bars_v5() -> None:
    dates = ["22/10/21", "23/10/21", "24/10/21", "25/10/21", "26/10/21"]
    z1 = np.array([20, 35, 30, 35, 27])
    z2 = np.array([25, 32, 34, 20, 25])
    z3 = np.array([20, 35, 30, 35, 27])
    z4 = np.array([25, 32, 34, 20, 25])
    z5 = np.array([20, 35, 30, 35, 27])

    width = 0.35  # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()

    ax.bar(dates, z1, width, color="0.8", label="Z1")
    ax.bar(dates, z2, width, color="b", label="Z2", bottom=z1)
    ax.bar(dates, z3, width, color="g", label="Z3", bottom=z1 + z2)
    ax.bar(dates, z4, width, color="tab:orange", label="Z4", bottom=z1 + z2 + z3)
    ax.bar(dates, z5, width, color="r", bottom=z1 + z2 + z3 + z4, label="Z5")

    ax.set_ylabel("Time in HR Zones")
    ax.set_title("HR Zones")
    ax.legend()

    plt.show()

if __name__ == "__main__":

    data_df = get_data()
    stack_bars_v1(data_df)
    # stack_bars_v2(data_df)
    # stack_bars_v3(data_df)
    # stack_bars_v4(data_df)
    # stack_bars_v5()
