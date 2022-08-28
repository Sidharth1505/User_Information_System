from utility.config import queries
from utility.connect import ConnectDb
from utility.validate import Validation
class Approve:
    def __init__(self,username):
        self.username = username
        self.view_list()
        self.approve_user()

    def view_list(self):
        query = queries['unapproved']
        record  = ConnectDb().fetch_data(query)
        print('username\tName')
        for i in record:
            print(f'{i[0]}\t{i[1]}')
    
    def approve_user(self):
        
        user_to_approve = input('Enter the username you want to approve : ')
        if Validation().if_exists(user_to_approve):
            query = queries['approve'].format( self.username,user_to_approve)
            ConnectDb().append_data_user(query)
            print('\n Approval Done !\n')
        else:
            print('Enter a Valid UserName from the List\n')

