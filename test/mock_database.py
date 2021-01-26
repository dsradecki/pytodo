from unittest import TestCase
import mysql.connector
from mysql.connector import errorcode
from mock import patch
import src.utils

MYSQL_USER = "root"
MYSQL_PASSWORD = "root"
MYSQL_DB = "testdb"
MYSQL_HOST = "127.0.0.1"


class MockDB(TestCase):

    @classmethod
    def setUpClass(cls):
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            buffered=True,
            auth_plugin='mysql_native_password'
        )
        cursor = connection.cursor(dictionary=True)

        # drop database if it already exists
        try:
            cursor.execute("DROP DATABASE {}".format(MYSQL_DB))
            cursor.close()
            print("DB dropped")
        except mysql.connector.Error as err:
            print("{}{}".format(MYSQL_DB, err))

        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(MYSQL_DB))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)
        connection.database = MYSQL_DB

        query = """CREATE TABLE tasks( 
	                id int(20) NOT NULL PRIMARY KEY,
                    task varchar(255),
                    description varchar(255),
                    deadline DATETIME
                )"""
        try:
            cursor.execute(query)
            connection.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("test_table already exists.")
            else:
                print(err.msg)


        cursor.close()
        connection.close()

        testconfig = {
            'host': MYSQL_HOST,
            'user': MYSQL_USER,
            'password': MYSQL_PASSWORD,
            'database': MYSQL_DB
        }
        cls.mock_db_config = patch.dict(src.utils.config, testconfig)

    @classmethod
    def tearDownClass(cls):
        cnx = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD
        )
        cursor = cnx.cursor(dictionary=True)

        # drop test database
        try:
            cursor.execute("DROP DATABASE {}".format(MYSQL_DB))
            cnx.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print("Database {} does not exists. Dropping db failed".format(MYSQL_DB))
        cnx.close()