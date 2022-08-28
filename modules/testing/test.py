import pytest
import unittest
from utility.connect import ConnectDb
from datetime import date

class Test(unittest.TestCase):
    def test_age(self):
        query = "SELECT date_of_birth from user_info_system.user where user_name = 'sid12'"
        data = ConnectDb().fetch_data(query)[0][0]
        today = date.today()
        age = today.year - data.year 
        self.assertEqual(21,age)

    def tes_call(self):
        unittest.main()




