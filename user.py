class User:
    '''
    generate new class instance of user
    '''
    user_list = []#empty user list
    def ___init___ (self,first_name,last_name,email,password):
        '''
        #_init_ method that defines our objects
        '''

        self.first_name= first_name
        self.last_name= last_name
        self.password= password
        self.email = email
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
    def user_registered(cls,user_name):
        '''
        Method that checks if a user exists in the user list.Will help in authentication
        '''

        for user in cls.user_list:
            if user.user_name == user_name:
                return True

            return false

