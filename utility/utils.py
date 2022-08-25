from utility.connect import ConnectDb

class Utility:
    def get_id_counter(self):
        query = "SELECT COUNT(id) from user_info_system.user"
        return ConnectDb().fetch_data(query)[0][0]
