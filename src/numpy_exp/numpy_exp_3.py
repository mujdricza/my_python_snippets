"""
https://www.w3schools.com/python/numpy/numpy_ufunc.asp

ufuncs stands for "Universal Functions" and they are NumPy functions that operate on the ndarray object.

ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.
    Converting iterative statements into a vector based operation is called vectorization.
    It is faster as modern CPUs are optimized for such operations.

They also provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation.

ufuncs also take additional arguments, like:
    where boolean array or condition defining where the operations should take place.
    dtype defining the return type of elements.
    out output array where the return value should be copied.
"""
from math import log

import numpy as np


def ufunc_intro_v1():
    x = [1, 2, 3, 4]
    y = [4, 5, 6, 7]
    z = np.add(x, y)  # elementwise addition
    print(z)
    # [ 5  7  9 11]

    # same outputs as:
    z = []
    for i, j in zip(x, y):
        z.append(i + j)
    print(z)
    # [5, 7, 9, 11]


def create_ufunc_v1():
    # To create your own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.
    #
    # The frompyfunc() method takes the following arguments:
    #   function - the name of the function.
    #   inputs - the number of input arguments (arrays).
    #   outputs - the number of output arrays.
    def myadd(x, y):
        return x+y

    myadd = np.frompyfunc(myadd, 2, 1)
    print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
    # [6 8 10 12]

    # type of ufunc: <class 'numpy.ufunc'>.
    print(type(np.add))
    print(type(np.concatenate))
    # <class 'numpy.ufunc'>
    # <class 'numpy._ArrayFunctionDispatcher'>

    if type(np.add) == np.ufunc:
        print("add is ufunc")
    else:
        print("add is not ufunc")
    # add is ufunc


def simple_arithmetic_v1():
    # You could use arithmetic operators + - * / directly between NumPy arrays, but this section discusses an extension of the same where we have functions that can take any array-like objects e.g. lists, tuples etc. and perform arithmetic conditionally.
    # All of the discussed arithmetic functions take a where parameter in which we can specify that condition.
    arr1 = np.array([10, 11, 12, 13, 14, 15])
    arr2 = np.array([20, 21, 22, 23, 24, 25])

    newarr = np.add(arr1, arr2)
    print(newarr)
    # [30 32 34 36 38 40]

    newarr = np.subtract(arr1, arr2)
    print(newarr)
    # [-10 -10 -10 -10 -10 -10]

    newarr = np.multiply(arr1, arr2)
    print(newarr)
    # [200 231 264 299 336 375]

    newarr = np.divide(arr1, arr2)
    print(newarr)
    # [0.5        0.52380952 0.54545455 0.56521739 0.58333333 0.6       ]

    newarr = np.power(arr1, arr2)
    print(newarr)
    # [ 7766279631452241920  3105570700629903195  5729018530666381312
    #  -4649523274362944347 -1849127232522420224  1824414961309619599]

    # Both the mod() and the remainder() functions return the remainder of the values in the first array corresponding to the values in the second array, and return the results in a new array.
    arr1 = np.array([10, 20, 30, 40, 50, 60])
    arr2 = np.array([3, 7, 9, 8, 2, 33])

    newarr = np.mod(arr1, arr2)
    print(newarr)
    # [ 1  6  3  0  0 27]

    # The divmod() function return both the quotient and the mod. The return value is two arrays, the first array contains the quotient and second array contains the mod.
    quot_arr, mod_arr = np.divmod(arr1, arr2)
    print(quot_arr)
    print(mod_arr)
    # [ 3  2  3  5 25  1]
    # [ 1  6  3  0  0 27]

    arr = np.array([-1, -2, 1, 2, 3, -4])
    newarr = np.absolute(arr)  # np.abs() is a non-preferred alternative
    print(newarr)
    # [1 2 1 2 3 4]


def round_decimals_v1():
    # There are primarily five ways of rounding off decimals in NumPy:
    #     truncation
    #     fix
    #     rounding
    #     floor
    #     ceil
    arr = np.trunc([-3.1666, 3.6667])
    print(arr)
    # [-3.  3.]

    arr = np.fix([-3.1666, 3.6667])
    print(arr)
    # [-3.  3.]

    arr = np.around(3.1666, 2)
    print(arr)
    # 3.17

    arr = np.floor([-3.1666, 3.6667])
    print(arr)
    # [-4.  3.]

    arr = np.ceil([-3.1666, 3.6667])
    print(arr)
    # [-3.  4.]


def logs_v1():
    # NumPy provides functions to perform log at the base 2, e and 10.
    # All of the log functions will place -inf or inf in the elements if the log can not be computed.

    arr = np.arange(1, 10)
    print(np.log2(arr))
    # [0.         1.         1.5849625  2.         2.32192809 2.5849625
    #  2.80735492 3.         3.169925  ]

    print(np.log10(arr))
    # [0.         0.30103    0.47712125 0.60205999 0.69897    0.77815125
    #  0.84509804 0.90308999 0.95424251]

    print(np.log(arr))  # log at base e
    # [0.         0.69314718 1.09861229 1.38629436 1.60943791 1.79175947
    #  1.94591015 2.07944154 2.19722458]

    # NumPy does not provide any function to take log at any base, so we can use the frompyfunc() function along with inbuilt function math.log() with two input parameters and one output parameter
    nplog = np.frompyfunc(log, 2, 1)
    print(nplog(100, 15))
    # 1.7005483074552052


def summation_v1():
    # Addition is done between two arguments whereas summation happens over n elements.
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([1, 2, 3])

    newarr = np.add(arr1, arr2)
    print(newarr)
    # [2 4 6]

    newarr = np.sum([arr1, arr2])  # without axis -> add up all elements
    print(newarr)
    # 12

    newarr = np.sum([arr1, arr2], axis=0)  # same as add (?)
    print(newarr)
    # [2 4 6]

    newarr = np.sum([arr1, arr2], axis=1)
    print(newarr)
    # [6 6]

    # Cummulative sum means partially adding the elements in array.
    # E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
    newarr = np.cumsum(arr1)
    print(newarr)
    # [1 3 6]


def products_v1():
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([5, 6, 7, 8])

    x = np.prod(arr1)
    print(x)
    # 24

    x = np.prod([arr1, arr2])
    print(x)
    # 40320

    newarr = np.prod([arr1, arr2], axis=0)
    print(newarr)
    # [ 5 12 21 32]

    newarr = np.prod([arr1, arr2], axis=1)
    print(newarr)
    # [  24 1680]

    newarr = np.cumprod(arr1)
    print(newarr)
    # [ 1  2  6 24]


def differences_v1():

    # A discrete difference means subtracting two successive elements.
    # E.g. for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]
    arr = np.array([10, 15, 25, 5])

    newarr = np.diff(arr)
    print(newarr)
    # [  5  10 -20]

    # We can perform this operation repeatedly by giving parameter n.
    # E.g. for [1, 2, 3, 4], the discrete difference with n = 2 would be [2-1, 3-2, 4-3] = [1, 1, 1] , then, since n=2, we will do it once more, with the new result: [1-1, 1-1] = [0, 0]
    newarr = np.diff(arr, n=2)
    print(newarr)
    # [  5 -30]


def lcm_v1():
    # LCM: The Lowest Common Multiple is the smallest number that is a common multiple of two numbers.
    num1 = 4
    num2 = 6

    x = np.lcm(num1, num2)
    print(x)
    # 12

    # To find the Lowest Common Multiple of all values in an array, you can use the reduce() method.
    arr = np.array([3, 6, 9])
    x = np.lcm.reduce(arr)
    print(x)
    # 18

    arr = np.arange(1, 11)
    x = np.lcm.reduce(arr)
    print(x)
    # 2520


def gcd_v1():
    # The GCD (Greatest Common Divisor), also known as HCF (Highest Common Factor) is the biggest number that is a common factor of both of the numbers.
    num1 = 6
    num2 = 9

    x = np.gcd(num1, num2)
    print(x)
    # 3

    # To find the Highest Common Factor of all values in an array, you can use the reduce() method.
    arr = np.array([20, 8, 32, 36, 16])

    x = np.gcd.reduce(arr)
    print(x)
    # 4


def trigonometric_functions_v1():
    # NumPy provides the ufuncs sin(), cos() and tan() that take values in radians and produce the corresponding sin, cos and tan values.

    x = np.sin(np.pi / 2)
    print(x)
    # 1.0

    arr = np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5])
    x = np.sin(arr)
    print(x)
    # [1.         0.8660254  0.70710678 0.58778525]

    # By default all of the trigonometric functions take radians as parameters but we can convert radians to degrees and vice versa as well in NumPy.
    # Note: radians values are pi/180 * degree_values.
    arr = np.array([90, 180, 270, 360])
    x = np.deg2rad(arr)
    print(x)
    # [1.57079633 3.14159265 4.71238898 6.28318531]

    arr = np.array([np.pi / 2, np.pi, 1.5 * np.pi, 2 * np.pi])
    x = np.rad2deg(arr)
    print(x)
    # [ 90. 180. 270. 360.]

    # Finding angles from values of sine, cos, tan. E.g. sin, cos and tan inverse (arcsin, arccos, arctan).
    # NumPy provides ufuncs arcsin(), arccos() and arctan() that produce radian values for corresponding sin, cos and tan values given.
    x = np.arcsin(1.0)
    print(x)
    # 1.5707963267948966

    arr = np.array([1, -1, 0.1])
    x = np.arcsin(arr)
    print(x)
    # [ 1.57079633 -1.57079633  0.10016742]

    # Finding hypotenues using pythagoras theorem in NumPy.
    # NumPy provides the hypot() function that takes the base and perpendicular values and produces hypotenues based on pythagoras theorem.
    base = 3
    perp = 4
    x = np.hypot(base, perp)
    print(x)
    # 5.0


def hyperbolic_func_v1():
    # NumPy provides the ufuncs sinh(), cosh() and tanh() that take values in radians and produce the corresponding sinh, cosh and tanh values.

    x = np.sinh(np.pi / 2)
    print(x)
    # 2.3012989023072947

    arr = np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5])
    x = np.cosh(arr)
    print(x)
    # [2.50917848 1.60028686 1.32460909 1.20397209]

    x = np.arcsinh(1.0)
    print(x)
    # 0.881373587019543

    arr = np.array([0.1, 0.2, 0.5])
    x = np.arctanh(arr)
    print(x)
    # [0.10033535 0.20273255 0.54930614]


def set_operations_v1():
    arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
    x = np.unique(arr)
    print(x)
    # [1 2 3 4 5 6 7]

    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([3, 4, 5, 6])

    newarr = np.union1d(arr1, arr2)
    print(newarr)
    # [1 2 3 4 5 6]

    newarr = np.intersect1d(arr1, arr2, assume_unique=True)  # Note: the intersect1d() method takes an optional argument assume_unique, which if set to True can speed up computation. It should always be set to True when dealing with sets.
    print(newarr)
    # [3 4]

    newarr = np.setdiff1d(arr1, arr2, assume_unique=True)
    print(newarr)
    # [1 2]

    # Finding Symmetric Difference
    # To find only the values that are NOT present in BOTH sets, use the setxor1d() method.
    newarr = np.setxor1d(arr1, arr2, assume_unique=True)
    print(newarr)
    # [1 2 5 6]


if __name__ == "__main__":
    # ufunc_intro_v1()
    # create_ufunc_v1()
    # simple_arithmetic_v1()
    # round_decimals_v1()
    # logs_v1()
    # summation_v1()
    # products_v1()
    # differences_v1()
    # lcm_v1()
    # gcd_v1()
    # trigonometric_functions_v1()
    # hyperbolic_func_v1()
    set_operations_v1()
