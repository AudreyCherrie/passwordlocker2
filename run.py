#!/usr/bin/env python3.6
from user import User
# from credentials import Credentials

def create_user(username,firstname,lastname,birthmonth,password):
    '''
    function to create a new account
    '''
    new_user = User(username,firstname,lastname,birthmonth,password)
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

def find_user_byPassword(password):
    '''
    This function will get a user's details using the password
    '''
    return User.find_user_byPassword(password)

def main():
    print(" Welcome to to the password locker.What is your name??")
    name = input()
    print(f"Welcome {name}  create an account ")
    # print("")

    while True:
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

        save_user(create_user(username,firstname,lastname,password)
        # print("/n")

        print (f"{firstname}{lastname} ,Your new account has been created")
        print("/n")
        print("Please login with your credentials")

        print("Enter Username")
        username = input()

        print("Enter password")
        password = input()

        if User.find_user_byPassword(password).password == password:
            print("Welcome .Press ds-to display passwords,ct-to create a new password, and dl to delete a password")
        elif User.find_user_byPassword(password).password != password:
            print("Wrong credetials")

if __name__ == '__main__':
    main()
