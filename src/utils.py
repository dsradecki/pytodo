import mysql
from src.database import get_db_connection, get_cursor
from settings import HOST, USER, PASSWORD, DB

from hashlib import md5

from argparse import ArgumentTypeError
from datetime import datetime

config = {
    'host': HOST,
    'user': USER,
    'password': PASSWORD,
    'database': DB
}


def write_to_db(query: str, values) -> bool:

    connection = get_db_connection(config)
    cursor = get_cursor(connection)

    #print("affected rows = {}".format(cursor.rowcount)) - use this to check 'ACKNOWLEDGMENT'

    try:
        cursor.execute(query, values)

    except (Exception, mysql.connector.Error) as e:
        print(e)
        return False

    connection.commit()
    connection.close()

    return True


def read_from_db(query: str) -> bool:

    connection = get_db_connection(config)
    cursor = get_cursor(connection)

    cursor.execute(query)

    entries = cursor.fetchall()
    cursor.close()
    connection.close()

    content = []

    for entry in entries:
        content.append(entry)

    return content


def valid_datetime(s: str):
    """

    Check whether the input string has DD-MM-YYYY-H:M format
    Rise ArgumentTypeError otherwise

    :param s: string to be checked
    :return: checked string
    """

    #Null is also a correct date since the user might prompt to enter task without a date provided
    if s == 'Null':
        return s

    try:
        return "%s" % datetime.strptime(s, "%d-%m-%Y-%H:%M")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s) \
              + "The date's valid format is 'DD-MM-YYYY-H:M'"

        raise ArgumentTypeError(msg)


def generate_hash(string: str) -> str:
    return md5(string.encode('utf-8')).hexdigest()


def generate_insert_query(dictionary: dict, table):
    placeholders = ', '.join(['%s'] * len(dictionary))
    columns = ', '.join(dictionary.keys())
    return "INSERT INTO %s ( %s ) VALUES ( %s )" % (table, columns, placeholders)
