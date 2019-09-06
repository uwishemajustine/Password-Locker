import unittest 
from credentials import credentials 

class Testcredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = credentials("alsenj20@yahoo.com","199b") # create credentials object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.twitter_account,"alsenj20@yahoo.com")
        self.assertEqual(self.new_credentials.password,"199b")
        
    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
         the credentials list
        '''
        self.new_credentials.save_credentials() 
        self.assertEqual(len(credentials.credentials_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        credentials.credentials_list = []


    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credentials
        objects to our credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = credentials("alsenj20@yahoo.com","199b") 
        test_credentials.save_credentials()
        self.assertEqual(len(credentials.credentials_list),2)


if __name__ == '__main__':
    unittest.main()