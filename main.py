from modules.auth.auth import UserAuthentication

class Main:
    def startup(self):
        print("==============WELCOME TO USER INFORMATION SYSTEM============\n")

        print('Enter 1 for Login \n')
        print('Enter 2 for SignIn \n')
        print("Enter 0 to exit\n")
        print('Enter Your Choice\n')

        choice = input("Enter your choice : ")
        if choice.isdigit() and  int(choice) == 1:
            UserAuthentication().login()
        elif choice.isdigit() and  int(choice) == 2:
            UserAuthentication().signup()
        elif choice.isdigit() and  int(choice) == 0:
            print("\n=================** THANK YOU FOR VISITING**===================\n")
            exit()
        else:
            print("Invalid choice, try again...")
            self.startup()

Main().startup()
