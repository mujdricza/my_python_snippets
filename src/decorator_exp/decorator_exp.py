"""
Simple decorator use with options for tracking the meta information.
Issue: When a function is decorated, the metadata of the original function is lost.
Solution: Python has a built-in function called functools.wraps that can be used to preserve the original function's name and docstring.

Example: Greeting a person with changing the input's case (lower/uppercasing).
- changecase() decorator gets metainfo from its myinner() function
- addgreeting() decorator gets metainfo from its own() function due to @functools.wraps

Learned from:
https://www.w3schools.com/python/python_decorators.asp

"""
import functools
from typing import Callable


def addgreeting(func):
    """Decorator keeping original function meta information."""

    @functools.wraps(func)  # to keep original function meta information of addgreeting()
    def myinner_g(name):
        return func(name) + " Have a good day!"

    return myinner_g


def changecase(change: str = "upper"):
    """Decorator with argument.
    Here used to control the changecase() functionality in code.

    :param change: change order; currently handled: "upper" (default), "lower".
    """

    def changecase(func: Callable[..., str]) -> Callable:
        """Changing case of the string result of func."""

        def myinner_c(name: str, *args, **kwargs):
            res: str = func(name, *args, **kwargs)
            if change == "lower":
                mod = res.lower()
            elif change == "upper":
                mod = res.upper()
            else:
                # not handled case
                mod = res
            return mod

        return myinner_c

    return changecase


# NOTE that order of the decorators does matter, changecase will be applied first, then addgreeting
@addgreeting
@changecase("lower")
def myfunction_not_fully_wrapped(myname: str) -> str:
    return f"Hello {myname}"

@addgreeting
def myfunction_wrapped(myname: str) -> str:
    return f"Hello {myname}"


def normal_function():
    """Doing nothing, just for comparison."""
    pass


if __name__ == '__main__':
    print("Using myfunction with 'John':")
    print(myfunction_wrapped("John"))
    print(myfunction_not_fully_wrapped("John"))
    print()
    print("Printing metainformation of the functions:")

    print(f"normal_function.__name__ = '{normal_function.__name__}'")
    # just for comparison: a function's __name__ is just its declared name

    print(f"myfunction_not_fully_wrapped.__name__ = '{myfunction_not_fully_wrapped.__name__}'")
    # result is myinner_c - if the metainfo of the function's decorator is not fixed, the metadata of the function gets lost.

    print(f"myfunction_wrapped.__name__ = '{myfunction_wrapped.__name__}'")
    # result is myfunction_wrapped - the metainfo of the function's decorator is fixed with @functools.wraps

    print(f"changecase.__name__ = '{changecase.__name__}'")
    print(f"addgreeting.__name__ = '{addgreeting.__name__}'")
    # result is changecase - the decorator function itself does not have the metadata issue with or without the @functools.wraps
