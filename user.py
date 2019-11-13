class User:
    '''
    generate new class instance of user
    '''
    user_list = []#empty user list
    def __init__ (self,username,firstname,lastname,email,password):
        '''
        #__init__ method that defines our objects
        '''

        self.username = username
        self.firstname= firstname
        self.lastname= lastname
        self.email = email
        self.password= password

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)


    @classmethod
    def find_user_byPassword(cls,password):
        '''
        This method will take in a password and check if the password exists to find the user
        '''

        for user in cls.user_list:
            if user.password == password:
                return user


    @classmethod
    def user_auth(cls,username,password):
        '''
        this method checks if the password matches the username 
        '''
        for user in cls.user_list:
            if user.username == username and user.password == password:
                return True


    @classmethod
    def user_registered(cls,user_name):
        '''
        Method that checks if a user exists in the user list.Will help in authentication
        '''

        for user in cls.user_list:
            if user.user_name == user_name:
                return True

            return false

