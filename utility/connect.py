from multiprocessing.dummy import connection
import mysql.connector
from utility.config import ls
from mysql.connector import Error

class ConnectDb:
    
    def __init__(self):
        self.connection = self.get_connection()

    def get_connection(self):
        try:
            connection = mysql.connector.connect(**ls)
            if connection.is_connected():
                return connection
        except Error as e:
            print('Error while connecting to the MySQL', e)


    def fetch_data(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def append_data_user(self,query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        