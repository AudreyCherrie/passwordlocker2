import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the  contact class behaviors.
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user=User("Audrey","Macharia","mish19")



    def tearDown(self):
        '''
        The tear down method which will clean up after every test case is complete
        '''

        User.user_list = []
        '''
        This will remove every test user instance after evry test case is complete
        '''


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Audrey")
        self.assertEqual(self.new_user.last_name,"Macharia")
        self.assertEqual(self.new_user.password,"mish19")

    def test_save_user(self):
        '''
        Test case to test if the user objects are saved 
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    # def test_save_multiple_USer(self):
    #     '''
    #     Testcase to test whether more than one user can be added to the user list
    #     '''

    #     self.new_user.save_users()
    #     test_user = User("Marion","Jones","jonne999")
    #     test_user.save_user()
    #     self.assertEqual(len(User.user_list),2)

    # def test_find_user_byPassword(self):
    #     '''
    #     To see if we can find he details of a user by using their username
    #     Will help us to match users to their passwords
    #     '''
    #     self.new_user.save_users()
    #     test_user = User("marion","Jones","jonne99")
    #     test_user.save_user()

    #     User_found = User.find_user_byPassword("jonne99")
    #     self.assertEqual(User_found.password,test_user.password)

    # def test_user_registered(self):
    #     '''
    #     To check if a user is already registered
    #     '''
    #     self.new_user.save_users()
    #     test_user = User("Marion","Jones","jonne99")
    #     test_user.save_user()

    #     user_registered = User.user_registered("Marion")
        
    #     self.assertTrue(user_registered)

    



    # # def test_save_user(self):
    # #     self.new_person.save_person()
    # #     self.assertEqual(len(User.user_list),1)

    if __name__=='__main__':
         unittest.main()
