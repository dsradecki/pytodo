import mysql.connector

USERNAME = "root"
HOST = "localhost"
DB_PASSWORD = "root"
DB = 'todoapp'


def perform_query(query: str):
    connection = get_db_conn()
    cursor = get_cursor(connection)

    try:
        cursor.execute(query)

    except (Exception, mysql.connector.Error) as e:
        return False, str(e)

    connection.commit()
    connection.close()

    return True, cursor.fetchone()


def get_cursor(db_conn):
    try:
        return db_conn.cursor()

    except (Exception, mysql.connector.Error) as e:
        print(str(e))
        return False


def get_db_conn():
    try:
        return mysql.connector.connect(host=HOST,
                                       user=USERNAME,
                                       password=DB_PASSWORD,
                                       buffered=True,
                                       database=DB)

    except (Exception, mysql.connector.Error) as e:
        print(str(e))
        return False

