"""
https://www.w3schools.com/python/pandas/default.asp

https://github.com/pandas-dev/pandas

"""
import os

import pandas as pd


DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "w3s_data")


def read_csv_v1():
    df = pd.read_csv("data.csv")
    print(df.to_string())


def simple_df_v1():
    # A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
    mydataset = {"cars": ["BMW", "Volvo", "Ford"], "passings": [3, 7, 2]}
    df = pd.DataFrame(mydataset)
    print(df)
    #     cars  passings
    # 0    BMW         3
    # 1  Volvo         7
    # 2   Ford         2

    data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
    }
    df = pd.DataFrame(data)
    print(df)
    #    calories  duration
    # 0       420        50
    # 1       380        40
    # 2       390        45


def simple_srs_v1():
    a = [1, 7, 2]
    myvar = pd.Series(a)
    print(myvar)
    # 0    1
    # 1    7
    # 2    2
    # dtype: int64

    print(myvar[0])
    # 1

    myvar = pd.Series(a, index=["x", "y", "z"])
    print(myvar)
    # x    1
    # y    7
    # z    2
    # dtype: int64

    print(myvar["y"])
    # 7


def keyvalue_srs_v1():

    calories = {"day1": 420, "day2": 380, "day3": 390}  # The keys of the dictionary become the labels.
    myvar = pd.Series(calories)
    print(myvar)
    # day1    420
    # day2    380
    # day3    390
    # dtype: int64

    myvar = pd.Series(calories, index=["day1", "day2"])
    print(myvar)
    # day1    420
    # day2    380
    # dtype: int64


def dataframe_loc_v1():
    data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
    }
    df = pd.DataFrame(data)
    print(df)
    #    calories  duration
    # 0       420        50
    # 1       380        40
    # 2       390        45

    # refer to the row index: -> returns a Pandas Series.
    print(df.loc[0])
    # calories    420
    # duration     50
    # Name: 0, dtype: int64

    # use a list of indexes:
    print(df.loc[[0, 1]])  # -> returns a Pandas DataFrame
    #    calories  duration
    # 0       420        50
    # 1       380        40


def named_indices_v1():

    data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}

    df = pd.DataFrame(data, index=["day1", "day2", "day3"])
    print(df)
    #       calories  duration
    # day1       420        50
    # day2       380        40
    # day3       390        45

    # refer to the named index:
    print(df.loc["day2"])
    # calories    380
    # duration     40
    # Name: day2, dtype: int64


def read_csv_v1():
    df = pd.read_csv(os.path.join(DATA_DIR, "data.csv"))
    print(df)  # If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows
    print(df.to_string())  # use to_string() to print the entire DataFrame.

    # The number of rows returned is defined in Pandas option settings.
    # You can check your system's maximum rows with the pd.options.display.max_rows statement.
    # In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.
    # You can change the maximum rows number with the same statement.
    print(pd.options.display.max_rows)
    pd.options.display.max_rows = 9999

    df = pd.read_csv(os.path.join(DATA_DIR, "data.csv"))
    print(df)


def read_json_v1():
    df = pd.read_json(os.path.join(DATA_DIR, "data.json"))
    print(df.to_string())

    # also from local json
    data = {
        "Duration": {"0": 60, "1": 60, "2": 60, "3": 45, "4": 45, "5": 60},
        "Pulse": {"0": 110, "1": 117, "2": 103, "3": 109, "4": 117, "5": 102},
        "Maxpulse": {"0": 130, "1": 145, "2": 135, "3": 175, "4": 148, "5": 127},
        "Calories": {"0": 409, "1": 479, "2": 340, "3": 282, "4": 406, "5": 300},
    }
    df = pd.DataFrame(data)
    print(df)
    #    Duration  Pulse  Maxpulse  Calories
    # 0        60    110       130       409
    # 1        60    117       145       479
    # 2        60    103       135       340
    # 3        45    109       175       282
    # 4        45    117       148       406
    # 5        60    102       127       300

    print(df.head(10))  # Get a quick overview by printing the first 10 rows of the DataFrame
    # if the number of rows is not specified, the head() method will return the top 5 rows

    print(df.tail())  # There is also a tail() method for viewing the last rows of the DataFrame.

    print(df.info())
    # e.g.
    # <class 'pandas.core.frame.DataFrame'>
    #   RangeIndex: 169 entries, 0 to 168
    #   Data columns (total 4 columns):
    #    #   Column    Non-Null Count  Dtype
    #   ---  ------    --------------  -----
    #    0   Duration  169 non-null    int64
    #    1   Pulse     169 non-null    int64
    #    2   Maxpulse  169 non-null    int64
    #    3   Calories  164 non-null    float64
    #   dtypes: float64(1), int64(3)
    #   memory usage: 5.4 KB
    #   None


if __name__ == "__main__":
    # read_csv_v1()
    # simple_df_v1()
    # simple_srs_v1()
    # keyvalue_srs_v1()
    # dataframe_loc_v1()
    named_indices_v1()
    read_json_v1()
    read_json_v1()
