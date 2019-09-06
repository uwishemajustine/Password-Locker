import unittest 
from personinfo import personinfo 

class Testpersoninfo(unittest.TestCase):

    '''
    Test class that defines test cases for the personinfo class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_personinfo = personinfo("Jasmine","Uwishema","8882","uwishema10@gmail.com") 


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_personinfo.login_name,"Jasmine")
        self.assertEqual(self.new_personinfo.username,"Uwishema")
        self.assertEqual(self.new_personinfo.password,"8882")
        self.assertEqual(self.new_personinfo.email,"uwishema10@gmail.com")

    def test_save_personinfo(self):
        '''
        test_save_personinfo test case to test if the personinfo object is saved into
         the personinfo list
        '''
        self.new_personinfo.save_personinfo() 
        self.assertEqual(len(personinfo.personinfo_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        personinfo.personinfo_list = []


    def test_save_multiple_personinfo(self):
        '''
        test_save_multiple_personinfo to check if we can save multiple personinfo
        objects to our personinfo_list
        '''
        self.new_personinfo.save_personinfo()
        test_personinfo = personinfo("Jasmine","Uwishema","8882","uwishema10@gmail.com") 
        test_personinfo.save_personinfo()
        self.assertEqual(len(personinfo.personinfo_list),2)

    def test_delete_personinfo(self):
                '''
                test_delete_personinfo to test if we can remove a personinfo from our personinfo list
                '''
                self.new_personinfo.save_personinfo()
                test_personinfo = personinfo("Jasmine","Uwishema","8882","uwishema10@gmail.com")
                test_personinfo.save_personinfo()

                self.new_personinfo.delete_personinfo()# Deleting a personinfo object
                self.assertEqual(len(personinfo.personinfo_list),1)

if __name__ == '__main__':
    unittest.main() 