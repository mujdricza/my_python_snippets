"""
https://www.w3schools.com/python/pandas/pandas_cleaning.asp
https://www.w3schools.com/python/pandas/pandas_correlations.asp
"""
import os

import pandas as pd


DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "w3s_data")


def cleaning_data_v1():
    df = pd.read_csv(os.path.join(DATA_DIR, "data_cleaning.csv"))

    # dropna(): removes all rows containing NULL values from the DataFrame.
    new_df = df.dropna()  # By default, the dropna() method returns a new DataFrame, and will not change the original.
    print(new_df.to_string())

    # df.dropna(inplace=True)  # changing the original df
    # print(df.to_string())

    # filling NULL values with another one
    new_df = df.fillna(130)

    # Replace NULL values in the "Calories" columns with the number 130
    df.fillna({"Calories": 130}, inplace=True)

    df = pd.read_csv(os.path.join(DATA_DIR, "data_cleaning.csv"))
    # using mean
    x = df["Calories"].mean()
    # or median
    x = df["Calories"].median()
    # or mode
    x = df["Calories"].mode()[0]  # print(df["Calories"].mode()) is a series -> first element contains the mode

    df_new = df.fillna({"Calories": x})  # Calculate the MEAN, and replace any empty values with it


def correct_format_v1():
    df = pd.read_csv(os.path.join(DATA_DIR, "data_cleaning.csv"))

    df["Date"] = pd.to_datetime(df["Date"], format="mixed")
    # NaN -> NaT (Not a Time)

    print(df.to_string())

    # just dropping the rows with NaN dates:
    df.dropna(subset=['Date'], inplace = True)

    # Set "Duration" = 45 in row 7:
    df.loc[7, 'Duration'] = 45

    # replace values with a condition
    for x in df.index:
        if df.loc[x, "Duration"] > 120:
            df.loc[x, "Duration"] = 120

    # or remove "drop" rows
    for x in df.index:
        if df.loc[x, "Duration"] > 120:
            df.drop(x, inplace=True)
    # EMM NOTE: index could be set again

    # discover duplicates:
    # Returns True for every row that is a duplicate, otherwise False
    print(df.duplicated())

    # and remove duplicated rows
    df.drop_duplicates(inplace = True)


def correlations_v1():
    df = pd.read_csv(os.path.join(DATA_DIR, "data.csv"))
    df.corr()

    # e.g.
    #             Duration     Pulse  Maxpulse  Calories
    #   Duration  1.000000 -0.155408  0.009403  0.922721
    #   Pulse    -0.155408  1.000000  0.786535  0.025120
    #   Maxpulse  0.009403  0.786535  1.000000  0.203814
    #   Calories  0.922721  0.025120  0.203814  1.000000

    # The corr() method ignores "not numeric" columns.
    # The number varies from -1 to 1.