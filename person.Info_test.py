import unittest # Importing the unittest module
from PersonInfo import Contact # Importing the contact class

class TestPersonInfo(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

     # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact = Contact("James","Muriuki","0712345678","james@ms.com") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual self.new_PersonInfo.login, "Maze")
        self.assertEqual(self.new_PersonInfo.username,"Uwishema")
        self.assertEqual(self.new_PersonInfo.password,"8844")
        self.assertEqual(self.new_PersonInfo.email,"justine89@gmail.com")


if __name__ == '__main__':
    unittest.main()
