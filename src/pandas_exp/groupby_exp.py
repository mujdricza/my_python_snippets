
import pandas as pd
import numpy as np


"""
df = pd.DataFrame(np.random.rand(4,4), columns=list('abcd'))
df['group'] = [0, 0, 1, 1]
df


          a         b         c         d  group
0  0.418500  0.030955  0.874869  0.145641      0
1  0.446069  0.901153  0.095052  0.487040      0
2  0.843026  0.936169  0.926090  0.041722      1
3  0.635846  0.439175  0.828787  0.714123      1

def max_min(x):
    return x.max() - x.min()

max_min.__name__ = 'Max minus Min'

df.groupby('group').agg({'a':['sum', 'max'],
                         'b':'mean',
                         'c':'sum',
                         'd': max_min})

              a                   b         c             d
            sum       max      mean       sum Max minus Min
group                                                      
0      0.864569  0.446069  0.466054  0.969921      0.341399
1      1.478872  0.843026  0.687672  1.754877      0.672401
"""


def max_min(x):
    return x.max() - x.min()


max_min.__name__ = 'Max minus Min'


def exp1():
    df = pd.DataFrame(np.random.rand(4, 4), columns=list('abcd'))
    df['group'] = [0, 0, 1, 1]
    print(df)

    df = df.groupby('group').agg({'a': ['sum', 'max'],
                             'b': 'mean',
                             'c': 'sum',
                             'd': max_min})

    print(df)


def exp2():
    df = pd.DataFrame(
        [
            {'name': "a", 'type': "b", 'int': "1"},
            {'name': "a", 'type': "c", 'int': "2"},
            {'name': "b", 'type': "b", 'int': "3"},
            {'name': "b", 'type': "c", 'int': "4"},
            {'name': "b", 'type': "c", 'int': "5"},
        ]
    )
    print(df)

    df = df.groupby('name').agg({'name':  set,  # [lambda x: x, set, list],
                                 'type': set,
                                 'int': list})
    df = df.reset_index(drop=True)
    df["name"] = df["name"].apply(lambda x: list(x)[0])
    df["len"] = df["int"].apply(lambda x: len(x))
    print(df)
    print(df.shape)
    print(df.columns)

    """
     python src/exp/pandas_exp/groupby_exp.py
      name type int
    0    a    b   1
    1    a    c   2
    2    b    b   3
    3    b    c   4
    4    b    c   5
      name    type        int  len
    0    a  {b, c}     [1, 2]    2
    1    b  {b, c}  [3, 4, 5]    3
    (2, 4)
    Index(['name', 'type', 'int', 'len'], dtype='object')
    """


def exp3():
    df = pd.DataFrame(
        [
            {'name': ["a"], 'type': "b", 'int': "1"},
            {'name': ["a", "b"], 'type': "c", 'int': "2"},
            {'name': ["b"], 'type': "b", 'int': "3"},
            {'name': ["b"], 'type': "c", 'int': "4"},
            {'name': ["b"], 'type': "c", 'int': "5"},
        ]
    )
    print(df)

    df["name"] = df["name"].apply(lambda x: tuple(x))

    df = df.groupby('name').agg({'name': set,  # [lambda x: x, set, list],
                                 'type': set,
                                 'int': list})
    df = df.reset_index(drop=True)
    df["name"] = df["name"].apply(lambda x: list(list(x)[0]))
    df["len"] = df["int"].apply(lambda x: len(x))
    print(df)
    print(df.shape)
    print(df.columns)

    """
         name type int
    0     [a]    b   1
    1  [a, b]    c   2
    2     [b]    b   3
    3     [b]    c   4
    4     [b]    c   5
         name    type        int  len
    0     [a]     {b}        [1]    1
    1  [a, b]     {c}        [2]    1
    2     [b]  {c, b}  [3, 4, 5]    3
    (3, 4)
    Index(['name', 'type', 'int', 'len'], dtype='object')
    """

if __name__ == '__main__':
    # exp1()
    # exp2()
    exp3()
