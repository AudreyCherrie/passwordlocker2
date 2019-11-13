#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

def create_user(username,firstname,lastname,email,password):
    '''
    function to create a new account
    '''
    new_user = User(username,firstname,lastname,email,password)
    return new_user

def save_user(User):
    '''
    Function saves a new user
    '''
    User.save_user()

def user_registered(password):
    '''
    This function will check if a given password exists in the user list
    '''
    return User.user_registered(password)

def authenticate_user(username,password):
    '''
    authenticates users when logging in
    '''
    return User.user_auth(username,password)  

def find_user_byPassword(password):
    '''
    This function will get a user's details using the password
    '''
    return User.find_user_byPassword(password)

def create_cred_for_existingfile(filename,email,password):
    '''
    function that creates credentials for existing user
    '''
    new_creds = Credentials(filename,email,password)
    return new_creds


def display_creds():
    '''
    this function will display the user credentials
    '''
    return Credentials.cred_display()
def save_creds(filename,email,password):
    '''
    this function saves the credentials
    '''
    return Credentials.save_creds (filename,email,password)

# def find_credential_byName()

def main():
    print(" Welcome to to the password locker.What is your name??")
    name = input()
    print(f"Welcome {name} now create an account ")
    

    print("Create your account")
    # print("")
    print("Enter a username ")
    username = input()

    print("First Name ...")
    firstname = input()

    print("Last Name ...")
    lastname = input()

    print("Your password...")
    password = input()

    print ("Your email...")
    email = input()
    save_user(create_user(username,firstname,lastname,email,password))

    # save_user(create_user(username,firstname,lastname,email,password))
                

    print(f" {firstname}......{lastname} ,Your new account has been created")
    print("\n")
    print("Please login with your credentials")

    print("Enter Username")
    username = input()

    print("Enter password")
    password = input()

    
    if authenticate_user(username,password):
        print(f"{username} welcome to your account")
        print("-"*70)
            
        while True:
                print("use the following shortcodes to navigate through the application")
                print("short_code::: ds -to display all your saved credentials, dc -to delete a credential, fc -find credential by filename, cc -save credentials of an existing account, nc - make credentials for a new account")
                code = input().lower()
                if code == 'cc':
                  print("saving credentials of an existing account or file")
                  print("please fill the required fields below")
                  print("enter the filename or account name...")
                  filename = input().lower()
                  print("enter your email address...")
                  c_email=input()
                  print("enter your password")
                  c_password = input()
                  save_creds(create_cred_for_existingfile(filename,email,password))
                  print(f"you have successfully saved your {filename} credentials.")
                elif code == 'dc':
                    print("enter the file name or account name of the credentials you want to delete")
                    del_filename = input().lower()
                    if existing_cred(del_filename):
                      del_Acc = find_cred_byfilename(del_filename)
                      delete_cred(del_Acc)
                      print(f"you have successfully deleted the {del_Acc.filename} account credentials")
                    else:
                      print("the above file name does not exist in your credential list")
                elif code =='fc':
                  print("enter the file name or account name of the credemtial account you searching for")
                  searchName = input().lower()
                  if existing_cred(searchName):
                    searchAcc = find_cred_byfilename(searchName)
                    print(f"your account is :::")
                    print("-"*20)
                    print(f"account name ..... {searchAcc.filename} ")
                    print(f"account passsword ..{searchAcc.password}")
                    print(f"email address ......{searchAcc.email}")
                  else:
                    print("the above account doesn't exist")
                elif code == 'ds':
                  # print('dd printing')
                  if display_creds() != '':
                    # print('dd printing sucess')
                    print(display_creds())
                    for cred in display_creds():
                      print(cred)
                      print(f"accountname::: {cred.filename} password::: {cred.password} email::: {cred.email}")
                  else:
                    print("you have no saved credentials")
                elif code == 'nc':
                  print("make credentials of a none exising account")
                  print("enter the filename or the account name of your new account..")
                  fname = input().lower()
                  print("enter email address")
                  n_email = input()
                  print("Do you want the application to generate a password for you?  enter YES: if you want the application to generate you a password.. NO: if you want to enter your own password ")
                  shortcode = input().lower()
                  if shortcode == 'yes':
                    passcode = n_email[:4] + "234"
                    print(f"your password is {passcode} ")
                  else:
                    print("enter your password")
                    passcode = input()
                    save_creds(create_cred_for_existingfile(fname,n_email,passcode))
                    print(f"you have succesfully created your new credentials for {fname} account")
    #   else:
    #     print("invalid username or password")
    # else:
    #   print("please fill all fields required.")
                  if User.find_user_byPassword(password).password == password:
                    print("Welcome .Press ds-to display passwords,ct-to create a new password, and dl to delete a password")
                elif User.find_user_byPassword(password).password != password:
                  print("invalid username or password")


if __name__ == '__main__':
    main()
