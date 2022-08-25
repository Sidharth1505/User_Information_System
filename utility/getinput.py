class GetInput:
    def get_input(self):
        record = {}
        record['Full_name'] = input('Enter the full name: ')
        record['date_of_birth'] = input('Enter the date of birth in format of yyyy-mm-dd ')
        record['phone_no'] = int(input('Enter the Phone No. of 10 digits : '))
        record['gender'] = input('Enter the Gender Male or Female : ')
        record['address'] = input('Enter the address : ')
        
        return record

        