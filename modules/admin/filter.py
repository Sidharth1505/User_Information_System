
from multiprocessing.sharedctypes import Value
from utility.config import queries
from utility.connect import ConnectDb
from utility.validate import Validation
from utility.config import mapping

class Filter:
    def __init__(self,username):
        print('\n=========WELCOME TO THE FILTER MENU ===============')
        self.menu_pop()
    
    def menu_pop(self):
        print('Enter 1 to view all users')
        print('Enter 2 to view specific user based on user_name')
        print('Enter 3 to view user based on specfic filter ')
        try:
            choice = int(input('Enter Your Choice : '))
            if choice == 1:
                self.show_all()
            elif choice ==2:
                self.show_specific()
            elif choice ==3:
                self.show_filter()
            else:
                print('Enter Valid Choice\n')
                self.menu_pop()
        except ValueError:
            print('Try Again !')
            self.menu_pop()

    def get_record(self,query):
        record = ConnectDb().fetch_data(query)
        if len(record)==0:
            print('No Record Found. Try Again')
        return record

    def show_all(self):
        query = queries['display_all_details']
        record = self.get_record(query)
        print('\n')
        for i in record:
            print(i)

    def show_specific(self):
        print('Select the username from the below list \n')
        record = ConnectDb().get_proc('getUserNames')
        print('\n')
        for i in record:
            print(i)
    
        username = input('\nEnter the UserName : ')
        if Validation().if_exists(username):
            query = queries['display_specific_user'].format(username)
            record = self.get_record(query)
            print('\n')
            for i in record:
                print(i)
                print('\n')
        else:
            print('Enter a Valid UserName from the List\n')

    def show_filter(self):
        print('Enter 1 to display based on Name : ')
        print('Enter 2 to display based on age : ')
        print('Enter 3 to display based on gender : ')
        print('Enter 4 to display based on Approval Status ')
        print('Enter 5 to display based on professions ')
        print('Enter 6 to display based on roles :')

        try:
            choice = int(input('\nEnter Your Choice :'))
            if choice <0 or choice>6:
                print('Wrong Input!! ')
            else:
                data = self.get_input(mapping[choice])
                query = queries['display_filter'].format(mapping[choice],data)
                record = self.get_record(query)
                print('\n')
                for i in record:
                    print(i)
                print('\n')
        except ValueError:
            print('Enter Valid Input ')

    def get_input(self,choice):
        if choice == 'year(sysdate())- year(date_of_birth)':
            print('Enter the age parameter :')
            data = input('Enter : ')
        else:
            print('Enter the choice based on {}'.format(choice.capitalize()))
            data = input('Enter : ')
        return data
