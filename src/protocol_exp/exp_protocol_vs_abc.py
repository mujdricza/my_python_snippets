"""
https://www.youtube.com/watch?v=dryNwWvSd4M

abc.ABC
- using inheritance

typing.Protocol
- inheritance not necessary, but possible
- relies on duck-typing -> issues, if exact types are needed/checked
- useful e.g. as parameter types (see do_write() and do_read() functions)


"""
import io
import os
from json import dumps as json_dumps
from json import loads as json_loads
from pickle import dumps as pickle_dumps
from pickle import loads as pickle_loads
from typing import Protocol, runtime_checkable


from abc import ABC, abstractmethod

############################ ABC

class SerializedFileHandler(ABC):

    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def serialize(self, data: dict) -> bytes:
        pass

    @abstractmethod
    def deserialize(self, data: bytes) -> dict:
        pass

    def write(self, data: dict) -> None:
        with open(self.filename, "wb") as f:
            f.write(self.serialize(data))

    def read(self) -> dict:
        with open(self.filename, "rb") as f:
            return self.deserialize(f.read())


class PickleHandler(SerializedFileHandler):
    def serialize(self, data: dict) -> bytes:
        return pickle_dumps(data)

    def deserialize(self, data: bytes) -> dict:
        return pickle_loads(data)


class JSONHanlder(SerializedFileHandler):
    def serialize(self, data: dict) -> bytes:
        return json_dumps(data).encode("utf-8")

    def deserialize(self, data: bytes) -> dict:
        return json_loads(data.decode("utf-8"))


def main_abc():
    data = {"name": "John Doe", "age": 30}

    path_pickle: str = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "data.pkl"
    )
    pickle_handler = PickleHandler(path_pickle)
    pickle_handler.write(data)
    print(pickle_handler.read())
    """{'name': 'John Doe', 'age': 30}"""

    path_json: str = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "data.json"
    )
    json_handler = JSONHanlder(path_json)
    json_handler.write(data)
    print(json_handler.read())
    """{'name': 'John Doe', 'age': 30}"""

    # some checks
    assert isinstance(pickle_handler, PickleHandler)
    assert isinstance(pickle_handler, SerializedFileHandler)
    assert isinstance(json_handler, JSONHanlder)
    assert isinstance(json_handler, SerializedFileHandler)


############### Protocol


@runtime_checkable
class Writable(Protocol):
    def write(self, data: dict) -> None:
        """This method should write dictionary data."""


class WritableWithInheritance(Protocol):
    @abstractmethod
    def write(self, data: dict) -> None:
        """This method should write dictionary data."""


@runtime_checkable
class Readable(Protocol):
    def read(self) -> dict:
        """This method should return dictionary data."""


def do_write(writer: Writable | WritableWithInheritance, data: dict) -> None:
    writer.write(data)  # works if writer has a write() function!


def do_read(reader: Readable) -> dict:
    return reader.read()


class Author:  # ~ our Writable for do_wriite()
    def __init__(self, name: str):
        self.name = name
        # NOTE: Author has no relation to Writable or Readable protocol objects

    def write(self, data: dict) -> None:
        """with same signature as Writable.write()"""
        print(f"{self.name} is writing {data}")


class AuthorWithInheritance(WritableWithInheritance):
    # makes sure that the important functions are there (here: write())
    def __init__(self, name: str):
        self.name = name
        # NOTE: Author has no relation to Writable or Readable protocol objects

    def write(self, data: dict) -> None:
        """with same signature as Writable.write()"""
        print(f"{self.name} is writing {data}")


def main_protocol():
    data = {"name": "John Doe", "age": 30}
    author = Author("John Doe")
    do_write(author, data)


def main_protocol_with_inheritance():
    data = {"name": "John Doe", "age": 30}
    author = AuthorWithInheritance("John Doe")
    do_write(author, data)


############################### further exp

def write(handler: Writable, data: dict) -> None:
    handler.write(data)


def read(handler: Readable) -> dict:
    return handler.read()


def main_further():
    data = {"name": "John Doe", "age": 30}

    path_pickle: str = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "data_further.pkl"
    )
    pickle_handler = PickleHandler(path_pickle)
    pickle_handler.write(data)
    print(pickle_handler.read())

    path_json: str = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "data_further.json"
    )
    json_handler = JSONHanlder(path_json)
    json_handler.write(data)
    print(json_handler.read())

    # some checks
    # if Writer and Reader are NOT annotated with @runtime_checkable --> TypeError: Instance and class checks can only be used with @runtime_checkable protocols
    # with @runtime_checkable decorator -> ok, but it is not a complete type check
    assert isinstance(pickle_handler, Writable)
    assert isinstance(json_handler, Readable)


def main_io():
    io_writer = io.BytesIO()

    # ok
    assert isinstance(io_writer, io.BytesIO)
    assert isinstance(io_writer, Writable)

    data = {"name": "John Doe", "age": 30}
    # not ok, since io.BytesIO nees bytes, and not dict as input -- type checking is not complete
    io_writer.write(data)


if __name__ == "__main__":
    main_abc()
    """
    {'name': 'John Doe', 'age': 30}
    {'name': 'John Doe', 'age': 30}
    """

    main_protocol()
    """
    John Doe is writing {'name': 'John Doe', 'age': 30}
    """
    main_protocol_with_inheritance()
    """
    John Doe is writing {'name': 'John Doe', 'age': 30}
    """

    main_io()

