from db import db_connection
import mysql.connector

db_connect = None


#  get connection and cursor from DB
def get_cursor():
    global db_connect
    global connection
    if db_connect == None:
        connection = mysql.connector.connect(user=db_connection.db_user,
                                             password=db_connection.db_password, host=db_connection.db_hostname,
                                             port=db_connection.db_port,
                                             database=db_connection.db_name, autocommit=True)

        db_connect = connection.cursor(buffered=True)
        return db_connect
    else:
        if connection.is_connected():
            return db_connect
        else:
            connection = None
            db_connect = None
            return get_cursor()
