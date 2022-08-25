from utility.connect import ConnectDb
from utility.validate import Validation
from utility.getinput import GetInput
from utility.utils import Utility
from utility.config import user_id,role_id
import maskpass
import hashlib

class UserAuthentication:

    def login(self):
        return True
    
    def signup(self):
        
        user_name = input('Enter the User Name')
        password = maskpass.askpass(prompt='Enter the Password : ', mask = '*')
        reenter_password = maskpass.askpass(prompt='Please enter the password again : ', mask='*')

        if password != reenter_password:
            print("Password Don't Match ")
            self.signup()
        elif not Validation().if_exists(user_name):
            print('User Name already exists')
            self.signup()
        else:
            password = password.encode('utf-8')
            hashed = hashlib.sha256(password).hexdigest()
            cursor = GetInput()
            record = cursor.get_input()
            usercount = user_id + Utility().get_id_counter()
            query = f"INSERT INTO user_info_system.user values({usercount},'{user_name}','{record['date_of_birth']}','{record['phone_no']}','{record['address']}','{hashed}', '{record['gender']}',0)"
            ConnectDb().append_data_user(query)

            query_for_role = f"INSERT INTO user_info_system.user_role_map values({usercount},{role_id})"
            ConnectDb().append_data_user_role(query_for_role)



