import mysql.connector
from mysql.connector import Error
import pandas as pd

#function to create sql server connection
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print(" connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


#function to perform every query
def perform_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
        
    except Error as err:
        print(f"Error: '{err}'")