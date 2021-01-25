from src.database import get_db_connection, get_cursor
from settings import HOST, USER, PASSWORD, DB
import mysql

config = {
    'host': HOST,
    'user': USER,
    'password': PASSWORD,
    'database': DB
}


def perform_query(query: str):

    connection = get_db_connection()
    cursor = get_cursor(connection)

    try:
        cursor.execute(query)

    except (Exception, mysql.connector.Error) as e:
        return False, str(e)

    connection.commit()
    connection.close()

    return True, cursor.fetchone()