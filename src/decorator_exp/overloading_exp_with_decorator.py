"""
Experimenting with @typing.overload decorator

https://typing.python.org/en/latest/spec/overload.html
"""

from typing import overload, Any, List


# make sure via @overload that input and output types are compatible
@overload
def my_func(x: int) -> int:
    ...


@overload
def my_func(x: str) -> str:
    ...


@overload
def my_func(x: List[Any]) -> str:
    ...


# There is always a last implementation without @overload decorator
# which actually contains the implementation
def my_func(x: str | int | List[Any]) -> str | int:
    input_type = type(x)

    match input_type:
        case __builtins__.int:
            return x
        case __builtins__.str:
            return x
        case __builtins__.list:
            return " ".join(list(map(str, x)))
        case _:
            raise NotImplementedError(f"Input type {input_type} is not expected.")


def use_overloaded_functions():

    a = "abc"
    i = 123
    l = [1, 2, 3]

    for element in [a, i, l]:
        res = my_func(element)
        print(f"Processing {type(element)} element -> result ({type(res)}): {res}")


if __name__ == "__main__":
    use_overloaded_functions()

"""
Processing <class 'str'> element -> result (<class 'str'>): abc
Processing <class 'int'> element -> result (<class 'int'>): 123
Processing <class 'list'> element -> result (<class 'str'>): 1 2 3
"""