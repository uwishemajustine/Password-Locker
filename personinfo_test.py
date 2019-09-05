import unittest 
from personinfo import personinfo 

class Testpersoninfo(unittest.TestCase):

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
        self.new_personinfo = personinfo("Uwishema","8844","justine89@gmail.com") 


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_personinfo.username,"Uwishema")
        self.assertEqual(self.new_personinfo.password,"8844")
        self.assertEqual(self.new_personinfo.email,"justine89@gmail.com")

    def test_save_personinfo(self):
        '''
        test_save_personinfo test case to test if the personinfo object is saved into
        the personinfo list
        '''
        self.new_personinfo.save_personinfo() 
        self.assertEqual(len(personinfo.personinfo_list),1)

if __name__ == '__main__':
    unittest.main()
