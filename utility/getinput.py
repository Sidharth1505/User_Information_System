from msvcrt import LK_LOCK
import math
class GetInput:
    def get_input(self):
        record = {}
        record['Full_name'] = input('Enter the full name: ')
        record['date_of_birth'] = input('Enter the date of birth in format of yyyy-mm-dd ')
        record['phone_no'] = GetInput().validate_input()
        record['gender'] = input('Enter the Gender Male or Female : ')
        record['address'] = input('Enter the address : ')
        profession = []
        i = 2
        while i>0:
            print('\nEnter 1  if you are a business man ')
            print('Enter 2  if you are a singer ')
            print('Enter 3 if you are a poet ')
            print('Enter 4 if you are a teacher')
            print('Enter 5 if you want to skip')
            try:
                choice = int(input('\nEnter your Choice : '))
                if choice ==5 and len(profession) !=0:
                    i-=1
                elif 0<choice <=4:
                    if choice not in profession:
                        profession.append(choice)
                        i-=1
                    else:
                        print('Entry already exists !')
                        continue
                else:
                    print('Enter valid Choice\n')
            except ValueError:
                print('Enter Number only\n')
        record['profession'] = profession
        return record
    
    def validate_input(self):
        user_input = input('Enter the Phone No. of 10 digits : ')
        try:
            user_input = int(user_input)
        except ValueError:
            print(f"Invalid")
            return GetInput().validate_input()
        else:
            if math.floor(math.log10(user_input)+1) == 10:
                return user_input
            print(f"Invalid !, please enter a valid 10 digit ")
            return GetInput().validate_input()


    def validate_mobile(self,user_input):
        if math.floor(math.log10(user_input)+1) == 10:
            return True
        else:
            return False
