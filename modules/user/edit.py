import imp
from utility.config import user_mapping
from utility.config import queries
from utility.connect import ConnectDb
class EditDetails:

    def __init__(self,username):
        self.view_my_details(username)
        self.menu(username)

    def view_my_details(self,username):
        query = queries['display_my_details'].format(username)
        record = ConnectDb().fetch_data(query)
        print('\n')
        for i in record:
            print(i)
        print('\n')

    def menu(self,username):
        print('Prompting for Edit Menu')
        print('Press 1 to edit your name')
        print('Press 2 to edit your date of birth')
        print('Press 3 to edit your contact')
        print('Press 4 to edit your address')  
        print('Press 5 to edit your gender')
        try:
            self.choice = int(input('Enter your choice\n'))
            self.modify_details(self.choice,username)
        except ValueError:
            print('Try Again !!')
            return
    def modify_details(self,choice,username):
        
        if choice == 1:
            updated_value = input('Enter the updated name : ')
        elif choice == 2:
            updated_value = input('Enter the updated date of birth in the format yyyy-mm-dd : ')
        elif choice == 3:
            updated_value = int(input('Enter the updated contact number : '))
        elif choice == 4:
            updated_value = input('Enter the updated address : ')
        elif choice == 5:
            updated_value = input('Enter the updated gender Male or Female : ')
        else:
            print('Invalid Choice')
            return
        query = queries['edit_user'].format(user_mapping[choice], updated_value, username,username)
        ConnectDb().append_data_user(query)
