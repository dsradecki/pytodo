import mysql.connector
from settings import USER, PASSWORD, DB, HOST


def get_cursor(db_conn):
    try:
        return db_conn.cursor()

    except (Exception, mysql.connector.Error) as e:
        print(str(e))
        return False


def get_db_connection():
    try:
        print(PASSWORD)
        return mysql.connector.connect(host=HOST,
                                       user=USER,
                                       password=PASSWORD,
                                       buffered=True,
                                       database=DB)

    except (Exception, mysql.connector.Error) as e:
        print(str(e))
        return False

