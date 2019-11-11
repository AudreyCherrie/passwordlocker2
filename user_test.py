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

    def test_save_multiple_USer(self):
        '''
        Testcase to test whether more than one user can be added to the user list
        '''

        self.new_user.save_users()
        test_user = User("Marion","Jones","jonne999")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_find_user_byPassword(self):
        '''
        To see if we can find he details of a user by using their username
        Will help us to match users to their passwords
        '''
        self.new_user.save_users()
        test_user = User("marion","Jones","jonne99")
        test_user.save_user()

        User_found = User.find_user_byPassword("jonne99")
        self.assertEqual(User_found.password,test_user.password)

    def test_user_registered(self):
        '''
        To check if a user is already registered
        '''
        self.new_user.save_users()
        test_user = User("Marion","Jones","jonne99")
        test_user.save_user()

        user_registered = User.user_registered("Marion")
        
        self.assertTrue(user_registered)

    
    def testcred_init(self):
        '''
        is a test case that tests if an object initialized properly
        '''
        self.assertEqual(self.new_cred.filename,"instagram")
        self.assertEqual(self.new_cred.password,"jonne99")


    def testCred_save(self):
        '''
        it tests if we can save a credential into our cred_list
        '''
        self.new_cred.save_cred()
        self.assertEqual(len(Credential.creds_list),1)


    def testmulti_cred_save(self):
        '''
        its a testcase that tests if multiple credentials can be saved
        '''
        self.new_cred.save_cred()
        test_cred = Credential("ig","jonne99")
        test_cred.save_cred()
        self.assertEqual(len(Credential.creds_list),2)

    def testDisplay_cred(self):
        '''
        this testcase tests returns all the credentials saved.
        '''
        self.assertEqual(Credential.cred_display(),Credential.creds_list)
    def testcred_exists(self):
        '''
        finds creditials using file name
        '''
        self.new_cred.save_cred()
        test_cred = Credential("ig","jonne99")
        test_cred.save_cred()
        cred_exists = Credential.cred_exist("ig")
        self.assertEqual(cred_exists.email,test_cred.email)


    def testDelete_cred(self):
        '''
        this testcase tests if a user can delete a username
        '''
        self.new_cred.save_cred()
        test_cred = Credential("ig","jonne99")
        test_cred.save_cred()
        cred_del = Credential.cred_exist(test_cred.filename)
        Credential.del_cred(cred_del)
        self.assertEqual(len(Credential.creds_list),1)


    def test_display_cred(self):
        '''
        this testcase tests if the credentials can be diplayed
        '''
        self.assertEqual(Credential.cred_display(),Credential.creds_list)



    # # def test_save_user(self):
    # #     self.new_person.save_person()
    # #     self.assertEqual(len(User.user_list),1)

    if __name__=='__main__':
         unittest.main()
