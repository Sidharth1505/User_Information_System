from msvcrt import LK_LOCK


class GetInput:
    def get_input(self):
        record = {}
        record['Full_name'] = input('Enter the full name: ')
        record['date_of_birth'] = input('Enter the date of birth in format of yyyy-mm-dd ')
        record['phone_no'] = int(input('Enter the Phone No. of 10 digits : '))
        record['gender'] = input('Enter the Gender Male or Female : ')
        record['address'] = input('Enter the address : ')
        profession = []
        i = 2
        while i>0:
            print('\nEnter 1  if you are a business man \n')
            print('Enter 2  if you are a singer \n')
            print('Enter 3 if you are a poet \n')
            print('Enter 4 if you are a teacher\n')
            print('Enter 5 if you want to skip \n')

            try:
                choice = int(input('Enter your Choice : '))
                if choice ==5 :
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