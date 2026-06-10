"""
https://www.youtube.com/watch?v=qkxf583t4Vc

railway:
- success or failure

recommendation: use railway-based programming only if meaningful (we except an error case)

pip install returns
- explicit handling of exceptions, None values
- most transparent code with @safe decorator

"""
from dataclasses import dataclass
import os

from returns.io import IO, IOFailure, IOResult, IOSuccess
from returns.maybe import Maybe, Nothing, Some
from returns.result import Failure, Result, Success, safe

### exp 1
def divide(a: int , b: int ) -> Result[int, str]:
    return Success(a // b) if b != 0 else Failure("Cannot divide by zero")


def main_divide() -> None:
    result = divide(10, 2).value_or("Error")
    error_result = divide(10, 0).value_or("Error")

    print(result)
    print(error_result)


def divide_v2(a: int , b: int ) -> Result[int, str]:
    try:
        return Success(a // b)
    except ZeroDivisionError:
        return Failure("Cannot divide by zero")


def main_divide_v2() -> None:
    result = divide_v2(10, 2)
    error_result = divide_v2(10, 0)

    print(result)
    print(error_result)

    print(divide_v2(10, 2).value_or(-1))
    print(divide_v2(10, 0).value_or(-1))


@safe
def divide_v3(a: int , b: int ) -> int:
    return a // b


def main_divide_v3() -> None:
    result = divide_v3(10, 2)
    error_result = divide_v3(10, 0)

    print(result)
    print(error_result)

    print(divide_v3(10, 2).value_or(-1))
    print(divide_v3(10, 0).value_or(-1))


######################### exp 2

@dataclass
class User:
    id: int
    name: str


USERS = {
    1: User(1, "Alice"),
    2: User(2, "Bob"),
}


def find_user_classic(user_id: int) -> User | None:
    if user_id not in USERS:
        # # option 1
        # raise ValueError
        # option 2
        return None
    return USERS[user_id]


# Using a Maybe container to handle optional values
def find_user(user_id: int) -> Maybe[User]:
    return Some(USERS.get(user_id)) if user_id in USERS else Nothing  # Nothing is a state <-> vs. None is a value


def handle_user_data(user_id: int) -> None:
    match find_user(user_id):
        case Some(user):
            print(f"User with id {user_id} found: '{user.name}'")
        case Nothing:
            print(f"User with id {user_id} not found.")


def main_user() -> None:
    result = find_user(1).map(lambda user: user.name)
    print(result)

    # graceful process
    missing_result = find_user(3).map(lambda user: user.name)
    print(missing_result)


def main_handle() -> None:
    handle_user_data(1)
    handle_user_data(3)


##################### exp 3

def parse_number(string: str) -> Result[int, str]:

    try:
        return Success(int(string))
    except ValueError:
        return Failure("Invalid number format")


def add_ten(number: int) -> Result[int, str]:
    return Success(number + 10)


def main_parse() -> None:
    result = parse_number("10").bind(add_ten)
    error_result = parse_number("NaN").bind(add_ten)

    print(result)
    print(error_result)


######################## exp 4


def read_file(file_path: str) -> IO[str]:
    with open(file_path, "r") as file:
        return IO(file.read())


def process_data(data: str) -> str:
    # Just a simple transformation for the example
    return data.upper()


def main_read_file() -> None:
    input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "user_data.txt")
    file_io: IO[str] = read_file(input_path)
    print(file_io)

    # do something with the data in the IO container
    processed_data = file_io.map(process_data)
    processed_data.map(lambda data: print(data))


def read_file_v2(file_path: str) -> IOResult[str, Exception]:
    try:
        with open(file_path, "r") as file:
            return IOSuccess(file.read())
    except IOError as e:
        return IOFailure(e)


def main_read_file_v2() -> None:
    file_io = read_file_v2("non-existing-file.txt")
    print(file_io)

    # do something with the data in the IO container
    processed_data = file_io.map(process_data)
    processed_data.map(lambda data: print(data))
    print(processed_data)


if __name__ == "__main__":
    print("main_divide:")
    main_divide()
    """5
    Error
    """

    print("main_divide_v2:")
    main_divide_v2()
    """
    <Success: 5>
    <Failure: Cannot divide by zero>
    5
    -1
    """

    print("main_divide_v3:")
    main_divide_v3()
    """
    <Success: 5>
    <Failure: integer division or modulo by zero>
    5
    -1
    """

    print("main_user:")
    main_user()
    """
    <Some: Alice>
    <Nothing>
    """

    print("main_handle:")
    main_handle()
    """
    User with id 1 found: 'Alice'
    User with id 3 not found.
    """

    print("main_parse:")
    main_parse()
    """
    <Success: 20>
    <Failure: Invalid number format>
    """

    print("main_read_file:")
    main_read_file()
    """
    <IO: user
    user
    user
    >
    USER
    USER
    USER

    """

    print("main_read_file_v2:")
    main_read_file_v2()
    """
    <IOResult: <Failure: [Errno 2] No such file or directory: 'non-existing-file.txt'>>
    <IOResult: <Failure: [Errno 2] No such file or directory: 'non-existing-file.txt'>>
    """
