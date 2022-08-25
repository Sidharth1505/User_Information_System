from utility.connect import ConnectDb
from utility.queries import queries

class Utility:
    def get_id_counter(self):
        query = queries['get_id_counter']
        return ConnectDb().fetch_data(query)[0][0]
