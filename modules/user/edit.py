import imp
from utility.config import user_mapping
from utility.queries import queries
from utility.connect import ConnectDb
class EditDetails:

    def __init__(self,username):
        self.view_my_details(username)
        self.menu()

    def view_my_details(self,username):
        query = queries['display_my_details'].format(username)
        record = ConnectDb().fetch_data(query)
        for i in record:
            print(i)
        print('\n')

    def menu(self):
        print('Press 1 to edit your name\n')
        print('Press 2 to edit your date of birth\n')
        print('Press 3 to edit your contact\n')
        print('Press 4 to edit your address\n')  
        print('Press 5 to edit your gender\n')
        try:
            self.choice = input('Enter your choice\n')
            self.modify_details(self.choice)
        except ValueError:
            print('Try Again !!')
    def modify_details(self,choice):
        
        if choice == '1':
            updated_value = input('Enter the updated name')
        elif choice == '2':
            updated_value = input('Enter the updated date of birth in the format yyyy-mm-dd')
        elif choice == '3':
            updated_value = int(input('Enter the updated contact number'))
        elif choice == '4':
            updated_value = input('Enter the updated address')
        elif choice == '5':
            updated_value = input('Enter the updated gender Male or Female')
        else:
            print('Invalid Choice')
            return
        query = queries['edit_user'].format(user_mapping[choice], updated_value, self.username,self.username)
        ConnectDb().append_data_user(query)

