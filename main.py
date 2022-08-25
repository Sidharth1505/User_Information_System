from utility.connect import ConnectDb

query = "select name from user_info_system.user where id = 101"

tmp = ConnectDb()
print(tmp.fetch_data(query))