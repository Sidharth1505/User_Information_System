import imp
from modules.admin.approve import Approve
from modules.admin.delete import Delete
from modules.admin.filter import Filter

class Admin:
    def __init__(self,username):
        self.username = username
        self.menu_pop_up()
    
    def menu_pop_up(self):
        while True:
            print('\nAdmin Functionalities :\n')
            print('Enter 1 for approve to user \n')
            print('Enter 2 to delete a user\n')
            print('Enter 3 for viewing the user details\n')
            print('Enter 4 for Exit')
            try:
                choice = int(input('Enter Your Choice : '))
                if choice == 1:
                    Approve(self.username)
                elif choice == 2:
                    Delete(self.username)
                elif choice ==3:
                    Filter(self.username)
                elif choice == 4:
                    print('Exiting')
                    exit()
                else:
                    print('Enter a Valid Input!')
                    self.menu_pop_up()
            except ValueError:
                print('Enter a valid input!')
                self.menu_pop_up()
