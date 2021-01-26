import mysql.connector


def get_cursor(db_conn):
    try:
        return db_conn.cursor()

    except (Exception, mysql.connector.Error) as e:
        print(str(e))
        return False


def get_db_connection(config):
    try:
        return mysql.connector.connect(**config)

    except (Exception, mysql.connector.Error) as e:
        print(str(e))
        return False
