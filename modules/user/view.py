from utility.config import queries
from utility.connect import ConnectDb
class View:
    def __init__(self,username):
        self.username = username
        print("=========VIEW MENU============")
        self.menu()
    
    def menu(self):
        print('Enter 1 to view your Own details')
        print('Enter 2 to view Other users')
        try:
            choice = int(input('\nEnter Your Choice :'))

            if choice ==1:
                self.view_my_details(self.username)
            elif choice ==2:
                self.display_other_user()
            else:
                print('Enter Valid Choice')
        except ValueError:
            print('Enter Valid Input')


    def view_my_details(self,username):
        query = queries['display_my_details'].format(username)
        record = ConnectDb().fetch_data(query)

        for i in record:
            print(i)
        print('\n')

    def display_other_user(self):
        query = queries['display_other']
        record = ConnectDb().fetch_data(query)

        for i in record:
            print(i)
        print('\n')
