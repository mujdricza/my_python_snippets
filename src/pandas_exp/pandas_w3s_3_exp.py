"""
https://www.w3schools.com/python/pandas/pandas_plotting.asp
"""
import os

import matplotlib.pyplot as plt
import pandas as pd


DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "w3s_data")


def plot_scatter_v1():
    df = pd.read_csv(os.path.join(DATA_DIR, "data.csv"))

    df.plot(kind="scatter", x="Duration", y="Calories")

    # plt.show()
    plt.savefig(os.path.join(DATA_DIR, "output_duration-calories_scatter.png"))

    plt.close()  # if not closed, the next plot would be drawn on the base of the previous one

    df["Duration"].plot(kind="hist")
    plt.savefig(os.path.join(DATA_DIR, "output_duration_hist.png"))



if __name__ == '__main__':
    plot_scatter_v1()
