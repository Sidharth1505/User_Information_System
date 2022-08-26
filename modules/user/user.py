from modules.user.edit import EditDetails
from modules.user.view import View

class User:
    def __init__(self,username):
        self.username = username
        self.menu_pop_up()
    
    def menu_pop_up(self):
        while True:
            print('\n==========WELCOME TO USER MENU===========')
            print('Enter 1 to view other users ')
            print('Enter 2 to edit your details')
            print('Enter 3 to Logout')
            try:
                choice = int(input('Enter Your Choice : '))
                if choice == 1:
                    EditDetails(self.username)
                elif choice == 2:
                    View(self.username)
                elif choice == 3:
                    print('Logging Out')
                    print('Migrating to Login Page ')
                    return
                else:
                    print('Enter a Valid Input!')
                    self.menu_pop_up()
            except ValueError:
                print('Enter a valid input!')
                self.menu_pop_up()
