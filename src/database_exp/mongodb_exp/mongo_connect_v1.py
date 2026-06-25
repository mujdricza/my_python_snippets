"""
Small script for connecting to MongoDB using pymongo.

Requirements: pip install pymongo

Documentation:
https://www.mongodb.com/docs/manual/tutorial/
https://www.mongodb.com/docs/manual/reference/connection-string/?deployment-type=atlas&interface-atlas-only=atlas-cli#connections-connection-options
https://www.prisma.io/dataguide/mongodb/connection-uris#a-quick-overview
"""
from typing import Any

from pymongo import MongoClient


def _get_connect_url(
    user: str | None,
    password: str | None,
    host: str,
    port: int | None,
    database: str | None,
) -> str:
    """Compile a standard MongoDB URL.

    Restrictions:
    - handling only one host
    - not including any parameters beyond authSource with the database name

    :param user: user name
    :param password: user's password
    :param host: host name
    :param port: port number
    :return: compiled connection URL
    """

    # mongodb://[username:password@]host[:port][,...hostN[:port]][/[database][?parameter_list]]
    user_password = "" if not (user or password) else user + ":" + password + "@"
    port = "" if not port else ":" + str(port)
    database_infos = "" if not database else "/"
    return f"mongodb://{user_password}{host}{port}/?authSource={database}"


def connection_exp_to_mongodb(
    user: str | None = "root",
    password: str | None = None,
    host: str = "localhost",
    port: int | None = 27017,
    database: str | None = "admin"
) -> MongoClient:
    """Connect to and disconnect from MongoDB, just for a minimal example.

    :param user: user name, defaults to "root"
    :param password: user's password, defaults to None
    :param host: host name, defaults to "localhost"
    :param port: port number, defaults to 27017
    :param database: database name, defaults to "admin"
    :return: the MongoDB connection
    """

    print("Connecting to mongoDB")
    connect_url = _get_connect_url(user, password, host, port, database)
    connection = MongoClient(connect_url)

    dbs = connection.list_database_names()
    print(f"List of databases: {dbs}")

    for db in dbs:
        print(f"Database: {db}")
    return connection


def small_experiment(
    mongodb_connection: MongoClient,
    database: str,
    collection: str
) -> None:

    db = mongodb_connection[database]
    cl = db[collection]

    docs = cl.find()  # just a simple command

    for doc in docs:
        print(f"Document: {doc}")


def close_connection(mongodb_connection: MongoClient) -> None:
    mongodb_connection.close()
    print("Connection closed")


def main(config: dict[str, Any]) -> None:
    connection = connection_exp_to_mongodb(**config)
    small_experiment(connection, "entertainment", "movies")
    close_connection(connection)


if __name__ == "__main__":
    example_1 = {
        "user": "root",
        "password": "<PASSWORD>",
        "host": "localhost",
        "port": 27017,
        "database": "entertainment"
    }
    example_2 = {"user": None,
                 "password": None,
                 "host": "localhost",
                 "port": 27017,
                 "database": "entertainment"
                 }
    # main(example_1)
    main(example_2)
