import unittest
from utility.connect import ConnectDb
from utility.getinput import GetInput

class Test(unittest.TestCase):
    def test_validate_mobile(self):
        assert True ==  GetInput().validate_mobile(124567890)

    def test_validate_mobile2(self):
        assert True ==  GetInput().validate_mobile(9729066397)
    
    

unittest.main()




