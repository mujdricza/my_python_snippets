"""
https://www.w3schools.com/python/numpy/default.asp
"""

import numpy as np

def basic_v1():
    arr = np.array([1,2,3,4,5])
    print(arr)  # [1 2 3 4 5]
    print(type(arr))  # <class 'numpy.ndarray'>


def basic_v2():
    arr = np.array([1, 2, 3, 4], ndmin=2)  # ndmin: prescribed dimension of the array
    print(arr)  # [[1 2 3 4]]
    print(arr.ndim)  # 2


def basic_v3():
    arr = np.array(42)
    print(arr)  # 42
    print(type(arr))  # <class 'numpy.ndarray'>
    print(arr.ndim)  # 0


def basic_v4():
    arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print("2nd element on 1st row: ", arr[0, 1])  # 2
    arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print("Last element from 2nd dim: ", arr[1, -1])  # 10


def slices_v1():
    # We pass slice instead of index like this: [start:end].
    # We can also define the step, like this: [start:end:step].

    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    print(arr[::2])  # [1 3 5 7]

    arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])  # [7 8 9]
    print(arr[1, 1:4])

    arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print(arr[0:2, 2])  # from both elements, take index 2: [3 8]


def types_v1():

    arr = np.array([1, 2, 3, 4])
    print(type(arr))  # type of the arr object: <class 'numpy.ndarray'>
    print(arr.dtype)  # type of the items in arr: int64

    arr = np.array(['apple', 'banana', 'cherry'])
    print(arr)  # ['apple' 'banana' 'cherry']
    print(arr.dtype)  # <U6

    arr = np.array([1, 2, 3, 4], dtype="S")
    print(arr)  # [b'1' b'2' b'3' b'4']
    print(arr.dtype)  # |S1

    # For i, u, f, S and U we can define size as well.
    arr = np.array([1, 2, 3, 4], dtype="i4")
    print(arr)
    print(arr.dtype)  # int32

    # The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.
    # The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.
    # The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the data type directly like float for float and int for integer.
    arr = np.array([1.1, 2.1, 3.1])
    # NOTE: "i", "i4" -> int32, "int", "i8" -> int64
    newarr = arr.astype("i")
    print(newarr)  # [1 2 3]
    print(newarr.dtype)  # int32

    arr = np.array([1, 0, 3])
    newarr = arr.astype(bool)
    print(newarr)  # [ True False  True]
    print(newarr.dtype)  # bool


def copy_and_view_v1():
    arr = np.array([1, 2, 3, 4, 5])
    print(arr)

    x = arr.copy()
    arr[0] = 42
    x[1] = 22

    print(arr)
    print(x)

    y = arr.view()
    arr[0] = 422
    y[4] = 55

    print(arr)
    print(x)
    print(y)
    # [1 2 3 4 5]
    # [42  2  3  4  5]
    # [ 1 22  3  4  5]
    # [422   2   3   4  55]
    # [ 1 22  3  4  5]
    # [422   2   3   4  55]

    print(arr.base)
    print(x.base)
    print(y.base)
    # None
    # None
    # [422   2   3   4  55]


def shape_v1():
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    print(arr.shape)

    arr = np.array([1, 2, 3, 4], ndmin=5)
    print(arr)
    print('shape of array :', arr.shape)

    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    newarr = arr.reshape(4, 3)
    print(newarr)
    print(f"{newarr.base=}")  # reshaping creates a view!

    newarr = arr.reshape(2, 3, 2)
    print(newarr)

    # (2, 4)
    # [[[[[1 2 3 4]]]]]
    # shape of array : (1, 1, 1, 1, 4)
    # [[ 1  2  3]
    #  [ 4  5  6]
    #  [ 7  8  9]
    #  [10 11 12]]
    # newarr.base=array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])
    # [[[ 1  2]
    #   [ 3  4]
    #   [ 5  6]]
    #
    #  [[ 7  8]
    #   [ 9 10]
    #   [11 12]]]

    # You are allowed to have one "unknown" dimension.
    # Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
    # Pass -1 as the value, and NumPy will calculate this number for you.
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    newarr = arr.reshape(2, 2, -1)
    print(newarr)
    print(newarr.shape)
    # [[[1 2]
    #   [3 4]]
    #
    #  [[5 6]
    #   [7 8]]]
    # (2, 2, 2)

    # Flattening array means converting a multidimensional array into a 1D array.
    # We can use reshape(-1) to do this.
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    newarr = arr.reshape(-1)
    print(newarr)
    print(newarr.shape)
    # There are a lot of functions for changing the shapes of arrays in numpy flatten, ravel and also for rearranging the elements rot90, flip, fliplr, flipud etc.
    newarr = arr.flatten()
    print(newarr)
    print(newarr.shape)
    print(newarr.base)  # flatten -> copy
    newarr = arr.ravel()
    print(newarr)
    print(newarr.shape)
    print(newarr.base)  # ravel -> view
    # [1 2 3 4 5 6]
    # (6,)
    # [1 2 3 4 5 6]
    # (6,)
    # None
    # [1 2 3 4 5 6]
    # (6,)
    # [[1 2 3]
    #  [4 5 6]]


def iter_v1():
    arr = np.array([[1, 2, 3], [4, 5, 6]])

    for x in arr:
        for y in x:
            print(y)
    print()
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6

    arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    for x in np.nditer(arr):
        print(x)
    print()
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8

    # We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.
    # NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].
    arr = np.array([1, 2, 3])
    for x in np.nditer(arr, flags=["buffered"], op_dtypes=["S"]):
        print(x)
    print(arr)
    print()
    # b'1'
    # b'2'
    # b'3'
    # [1 2 3]

    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    for x in np.nditer(arr[:, ::2]):
        print(x)
    print()
    # 1
    # 3
    # 5
    # 7

    for idx, x in np.ndenumerate(arr):
        print(idx, x)
    print()
    # (0, 0) 1
    # (0, 1) 2
    # (0, 2) 3
    # (0, 3) 4
    # (1, 0) 5
    # (1, 1) 6
    # (1, 2) 7
    # (1, 3) 8


def join_v1():
    # In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr = np.concatenate((arr1, arr2))
    print(arr)
    # [1 2 3 4 5 6]

    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    arr = np.concatenate((arr1, arr2), axis=0)
    print(arr)
    # [[1 2]
    #  [3 4]
    #  [5 6]
    #  [7 8]]
    arr = np.concatenate((arr1, arr2), axis=1)
    print(arr)
    # [[1 2 5 6]
    #  [3 4 7 8]]

    # Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr = np.stack((arr1, arr2), axis=1)
    print(arr)
    # [[1 4]
    #  [2 5]
    #  [3 6]]

    # NumPy provides a helper function: hstack() to stack along rows.
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr = np.hstack((arr1, arr2))
    print(arr)
    # [1 2 3 4 5 6]

    # NumPy provides a helper function: vstack()  to stack along columns.
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr = np.vstack((arr1, arr2))
    print(arr)
    # [[1 2 3]
    #  [4 5 6]]

    # NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr = np.dstack((arr1, arr2))
    print(arr)
    # [[[1 4]
    #   [2 5]
    #   [3 6]]]


def split_v1():
    arr = np.array([1, 2, 3, 4, 5, 6])
    newarr = np.array_split(arr, 3)
    print(newarr)
    print(type(newarr))
    print(type(newarr[0]))
    # [array([1, 2]), array([3, 4]), array([5, 6])]
    # <class 'list'>
    # <class 'numpy.ndarray'>

    # using array_split(), if the array has less elements than required, it will adjust from the end accordingly.
    # The return value of the array_split() method is a list containing each of the split as an array.
    # We also have the method split() available but it will not adjust the elements when elements are less in source array for splitting like in example above, array_split() worked properly but split() would fail.
    arr = np.array([1, 2, 3, 4, 5, 6])
    newarr = np.array_split(arr, 4)
    print(newarr)
    # [array([1, 2]), array([3, 4]), array([5]), array([6])]
    newarr = np.array_split(arr, 8)
    print(newarr)
    print(newarr[0].shape)
    print(newarr[7].shape)
    # [array([1]), array([2]), array([3]), array([4]), array([5]), array([6]), array([], dtype=int64), array([], dtype=int64)]
    # (1,)
    # (0,)

    arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
    newarr = np.array_split(arr, 3)
    print(newarr)
    # [array([[1, 2],
    #        [3, 4]]),
    #  array([[5, 6],
    #        [7, 8]]),
    #  array([[ 9, 10],
    #        [11, 12]])]

    arr = np.array(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
    )
    newarr = np.array_split(arr, 3, axis=1)
    print(newarr)
    # [array([[ 1],
    #        [ 4],
    #        [ 7],
    #        [10],
    #        [13],
    #        [16]]),
    # array([[ 2],
    #        [ 5],
    #        [ 8],
    #        [11],
    #        [14],
    #        [17]]),
    #  array([[ 3],
    #        [ 6],
    #        [ 9],
    #        [12],
    #        [15],
    #        [18]])]

    # An alternate solution is using hsplit() opposite of hstack()
    # Use the hsplit() method to split the 2-D array into three 2-D arrays along columns.
    newarr = np.hsplit(arr, 3)
    print(newarr)
    # [array([[ 1],
    #        [ 4],
    #        [ 7],
    #        [10],
    #        [13],
    #        [16]]),
    #  array([[ 2],
    #        [ 5],
    #        [ 8],
    #        [11],
    #        [14],
    #        [17]]),
    #  array([[ 3],
    #        [ 6],
    #        [ 9],
    #        [12],
    #        [15],
    #        [18]])]

    # Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().


def search_v1():
    arr = np.array([1, 2, 3, 4, 5, 4, 4])
    x = np.where(arr == 4)
    print(x)
    # (array([3, 5, 6]),)

    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    x = np.where(arr % 2 == 0)
    print(x)
    # (array([1, 3, 5, 7]),)

    # There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
    # The searchsorted() method is assumed to be used on sorted arrays.
    # By default the left most index is returned, but we can give side='right' to return the right most index instead.
    arr = np.array([6, 7, 8, 9])
    x = np.searchsorted(arr, 7)
    print(x)
    # 1
    x = np.searchsorted(arr, 7, side="right")
    print(x)
    # 2

    arr = np.array([1, 3, 5, 7])
    x = np.searchsorted(arr, [2, 4, 6])
    print(x)
    # [1 2 3]


def sort_v1():

    # sort() This method returns a copy of the array, leaving the original array unchanged.
    arr = np.array([3, 2, 0, 1])
    newarr = np.sort(arr)
    print(arr)
    print(newarr)
    # [3 2 0 1]
    # [0 1 2 3]

    arr = np.array(["banana", "cherry", "apple"])
    print(np.sort(arr))
    # ['apple' 'banana' 'cherry']

    # If you use the sort() method on a 2-D array, both arrays will be sorted:
    arr = np.array([[6, 2, 4], [5, 0, 1]])
    print(np.sort(arr))
    # [[2 4 6]
    #  [0 1 5]]


def filter_v1():
    # In NumPy, you filter an array using a boolean index list.
    # A boolean index list is a list of booleans corresponding to indexes in the array.
    # If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.
    arr = np.array([41, 42, 43, 44])
    x = [True, False, True, False]
    newarr = arr[x]
    print(newarr)
    # [41 43]

    # We can directly substitute the array instead of the iterable variable in our condition and it will work just as we expect it to.
    arr = np.array([41, 42, 43, 44])
    filter_arr = arr > 42
    newarr = arr[filter_arr]
    print(filter_arr)
    print(newarr)
    # [False False  True  True]
    # [43 44]
    

if __name__ == "__main__":
    # basic_v1()
    # basic_v2()
    # basic_v3()
    # basic_v4()
    # slices_v1()
    # types_v1()
    # copy_and_view_v1()
    # shape_v1()
    # iter_v1()
    # join_v1()
    # split_v1()
    # search_v1()
    # sort_v1()
    filter_v1()
