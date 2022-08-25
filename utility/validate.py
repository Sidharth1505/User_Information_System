from utility.connect import ConnectDb

class Validation:

    def is_user(self):
        return True

    def if_exists(self, username):
        instance = ConnectDb()
        query = f"SELECT COUNT(name) from user_info_system.user where name = '{username}'"
        count = instance.fetch_data(query)[0][0]
        return count == 0



