from utility.connect import ConnectDb
from utility.validate import Validation
from utility.getinput import GetInput
from utility.utils import Utility
from utility.config import user_id,role_id
from utility.queries import queries
from modules.admin.admin import Admin
from modules.user.user import User
from datetime import datetime
import maskpass
import hashlib

class UserAuthentication:

    def login(self):
        username = input('Enter the username : ')
        password = maskpass.askpass(prompt = 'Enter the password :', mask = '*')
        password = password.encode('utf-8')
        check_password = hashlib.sha256(password).hexdigest()
        if len(username or password) <1:
            print('Enter Valid Input !')
            self.login()
        try:
            if Validation().if_exists(username):
                if Validation().valid_user(username, check_password) and Validation().is_allowed(username):
                    print('Login Success')
                    if Validation().is_user(username):
                        User(username)
                    else:
                        Admin(username)
                else:
                    print('Login Failed')
                    self.login()
            else:
                print(Validation().if_exists(username))
                print('Access Denied !! \n Try Again ')
                return
        except ValueError:
            print("Try Again !!")
            return

    
    def signup(self):

        user_name = input('Enter the User Name: ')
        password = maskpass.askpass(prompt='Enter the Password : ', mask = '*')
        reenter_password = maskpass.askpass(prompt='Please enter the password again : ', mask='*')

        if password != reenter_password:
            print("Password Don't Match ")
            self.signup()
        elif Validation().if_exists(user_name):
            print('User Name already exists')
            self.signup()
        else:
            password = password.encode('utf-8')
            hashed = hashlib.sha256(password).hexdigest()
            record = GetInput().get_input()
            usercount = user_id + Utility().get_id_counter()
            query = queries['insert_user'].format(usercount,user_name,record['Full_name'],record['date_of_birth'],record['phone_no'],record['address'],hashed, record['gender'],0,user_name)
            ConnectDb().append_data_user(query)

            query_for_role = queries['insert_user_map'].format(usercount,role_id)
            ConnectDb().append_data_user(query_for_role)
            if len(record['profession'])>1:
                query_for_profession = queries['insert_profession_map'][0].format(usercount,record['profession'][0],usercount,record['profession'][1])
            else:
                query_for_profession = queries['insert_profession_map'][1].format(usercount, record['profession'][0])
            ConnectDb().append_data_user(query_for_profession)



