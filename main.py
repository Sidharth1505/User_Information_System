
from modules.auth.auth import UserAuthentication
from modules.testing.test import Test
from utility.queries import GetJson

class Main:
    def startup(self):
        print("\n\n==============WELCOME TO USER INFORMATION SYSTEM============\n")

        print('Enter 1 for Login ')
        print('Enter 2 for SignUp ')
        print('Enter 3 for test module ')
        print("Enter 0 to exit")
        print('Enter Your Choice\n')

        choice = input("Enter your choice : ")
        if choice.isdigit() and  int(choice) == 1:
            UserAuthentication().login()
        elif choice.isdigit() and  int(choice) == 2:
            UserAuthentication().signup()
        elif choice.isdigit() and int(choice) == 3:
            Test().tes_call()
        elif choice.isdigit() and  int(choice) == 0:
            print("\n=================** THANK YOU FOR VISITING**===================\n")
            exit()
        else:
            print("Invalid choice, try again...")
            self.startup()

while True:
    Main().startup()





