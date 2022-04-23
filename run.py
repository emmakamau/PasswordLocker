#!/usr/bin/env python3.8

from credentials import Credential
from user import User

#Create new user
def create_user(username,password,credential:Credential):
    new_user = User(username,password,credential)
    return new_user

#Save user
def save_user(user):
    user.save_user()

#Delete user
def del_user(user):
    user.delete_user()

#Check if user exists
def user_exist(user):
    return User.user_exists(user)

#Create credential
def create_credential(account,username,email,password):
    new_credential = Credential(account,username,email,password)
    return new_credential

#Save Credential
def save_credential(credential):
    credential.save_credential()

#Delete credential
def del_credential(credential):
    credential.delete_credential()

#Find account in credentials
def find_credential(account):
    return Credential.find_by_account(account)

#Check existing credential
def credential_exist(account):
    return Credential.credential_exist(account)

#Display all credentials for a particular user
def display_credential():
    return Credential.display_credentials()


""" Define main function that calls the rest of the functions """

def passwordLocker():
    print("Hello, Welcome to Password Locker. Do you have an account with us? shortcode: yes or no")
    acc_available_ans = input().lower()
    
    if acc_available_ans == "yes":
        username = input("Enter Username: ")
        password = input("Enter password: ")

        if user_exist(username):
            User.password = password
            print("Login successful")
            print("\n")
            print("Use these short codes : cc - create a new credential, dc - display credential, fc -find a credential, ex -exit the credential list")
        else:
            print("\n")
            print("User does not exist")
    elif acc_available_ans == "no":
        print("Use these short codes : cc - create a user account, ex - Exit the application")

    else:
        print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
    passwordLocker()