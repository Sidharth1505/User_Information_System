from unittest import result
from utility.connect import ConnectDb
from utility.queries import queries
class Validation:
    def __init__(self):
        self.instance = ConnectDb()

    def is_user(self,username):
        query = queries['is_user'].format(username)
        record = self.instance.fetch_data(query)[0][0]
        return record == 'user'


    def if_exists(self, username):
        query = queries['if_exists'].format(username)
        count = self.instance.fetch_data(query)[0][0]
        return count != 0

    def valid_user(self,username, password):
        query = queries['check_password'].format(username)
        result = self.instance.fetch_data(query)[0][0]
        return result == password

    def is_allowed(self,username):
        query = queries['is_allowed'].format(username)
        result = self.instance.fetch_data(query)[0][0]
        return result == 1

