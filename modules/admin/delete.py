from utility.config import queries
from utility.connect import ConnectDb
from utility.validate import Validation

class Delete:
    def __init__(self,username):
        self.username = username
        print('\n==============WELCOME TO DELETE MENU=============\n')

        self.menu_pop()
    
    def menu_pop(self):
        print('Enter the user name from the below list you want to delete !')
        query = queries['display_all_username']
        record = ConnectDb().fetch_data(query)
        print('\n')
        for i in record:
            print(i)
        print('\n')

        choice = input('Enter the username you decided to delete :')
        if Validation().if_exists(choice) and choice != self.username:
            query = queries['delete_user'].format(choice)
            ConnectDb().append_data_user(query)
        else:
            print('Enter a valid username')




