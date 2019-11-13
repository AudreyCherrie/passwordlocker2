class Credentials :
        
        '''
        this class helps generates credentials for the user
        '''
        creds_list = [] # empty credential list
        def __init__(self,filename,email,password):
                '''
                #_init_ method that defines our objects
                '''

                self.filename= filename
                self.password= password
                self.email = email
                
        def save_creds(self):
                '''
                this  method saves credentials objects into cred_list
                '''
                Credentials.creds_list.append(self)

        def delete_user(self):
                '''
                this  method deletes credentials objects into cred_list
                '''
                Credentials.creds_list.remove(self)  

        @classmethod
        def cred_exixst(cls,filename):
                '''
                this method checks if a crtain filename exists
                '''
                for cred in cls.creds_list:
                        if cred.filename == filename:
                                return cred



        @classmethod
        def  cred_display(cls):
                '''
                returns the user list
                '''
        
                return cls.creds_list

        @classmethod
        def find_credential_byName(cls,del_filename):
                '''
                return a boolean if a credential    exist
                '''
                for cred in cls.creds_list:
                        if cred.filename == del_filename:

                                return True
                return False     

               