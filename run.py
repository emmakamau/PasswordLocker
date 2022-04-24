#!/usr/bin/env python3.8

from string import digits
from credentials import Credential
from user import User
import random
import array

#Password generator - https://www.geeksforgeeks.org/generating-strong-password-using-python/
def password_gen():
    max_len = 8
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lower_case_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
    upper_case_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']
    
    symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
            '*', '(', ')', '<']

    put_together = digits + upper_case_characters + lower_case_characters + symbols

    rand_digit = random.choice(digits)
    rand_upper = random.choice(upper_case_characters)
    rand_lower = random.choice(lower_case_characters)
    rand_symbol = random.choice(symbols)

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(max_len - 4):
        temp_pass = temp_pass + random.choice(put_together)
 
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password = password + x
    return password

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

#Find user
def find_user(user):
    return User.find_user(user)

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
    error_response = "I really didn't get that. Please use the short codes"
    bye_msg = "Bye bye, It was nice having you here."
    page_separator = "-"*60
    new_line = "\n"
    
    while True:
        print(new_line)
        print("Hello, Welcome to Password Locker. Do you have an account with us? Answer with yes or no")
        acc_available_ans = input().lower()
        if acc_available_ans == "yes":
            username = input("Enter Username: ").lower()
            password = input("Enter password: ")
        
            if user_exist(username):
                search_user = find_user(username)
                response = search_user.capitalize()
                print(page_separator)
                print(f"Hey, {response} Login is successful")
                print(page_separator)
                while True:
                    print(new_line)
                    print("Use these short codes : cc - create a new credential, dc - display credential, fc -find a credential, ex -exit the credential list")
                    shortcode = input().lower()
                    if shortcode == "cc":
                        print("New Credentials")
                        print(page_separator)
                        account = input("Enter account type e.g facebook: ").lower()
                        username = input("Enter username for account: ")
                        email = input("Enter email account used for account registration: ")

                        print(f"Would you like to generate a password for your {account} account? yes or no")
                        preference = input().lower()
                        if preference == "yes":
                            password = str(password_gen())
                            print(page_separator)
                        elif preference == "no":
                            password = input("Enter password for the account: ")
                        else:
                            print(error_response)
                        save_credential(create_credential(account,username,email,password))
                        print(f"Credentials for {account} have been saved.")
                        print(new_line)
                    elif shortcode == "dc":
                        if display_credential():
                            print("Here is a list of all your saved credentials:")
                            print(page_separator)
                            print("Here is a list of your credentials:")
                            print(new_line)
                            for credential in Credential.credential_list:
                                print(f"Account:{credential.account}, Username:{credential.username}, Email:{credential.email}, Password:{credential.password}")
                            print(page_separator)
                        else:
                            print("No credentials have been added")
                    elif shortcode == "fc":
                        search = input("Enter account name you are searching for: ").lower()
                        if credential_exist(search):
                            search_acc = find_credential(search)
                            print(page_separator)
                            print(f"Account:{search_acc.account}, Username:{search_acc.username},Email:{search_acc. email}, Password:{search_acc.password}")
                            print(page_separator)
                        else:
                            print("Credential does not exist")
                    elif shortcode == "ex":
                        input("Type ex to confirm exit: ")
                        return
                    else:
                        print(error_response)
            else:
                print(new_line)
                print("User does not exist")
                print(new_line)
        elif acc_available_ans == "no":
            print("\n")
            print("Use these short codes : cc - create a user account, ex - Exit the application")
            shortcode = input().lower()
            if shortcode == "cc":
                username = input("Enter your username: ").lower()
                show_username = username.capitalize()
                if user_exist(username):
                    search_user = find_user(username)
                    print("Username exists, use another username")
                else:
                    print(new_line)
                    print("Would you like a system generated password? Shortcode: yes or no")
                    shortcode = input().lower()
                    if shortcode == "yes":
                        password = password_gen()
                        print(page_separator)
                    elif shortcode == "no":
                        password = input("Enter password: ")
                    else:
                        print(error_response)
                    save_user(create_user(username,password,[]))
                    print(f"Hey {show_username},Let's log you in and add some credentials for safe keeping.")
                    print(f"Kindly take note of your password : {password}")
                    print(page_separator)
            elif shortcode == "ex":
                print(bye_msg)
                break
        else:
            print(error_response)




if __name__ == '__main__':
    passwordLocker()


"""
print("Use these short codes : cc - create a new credential, dc - display credential, fc -find a credential, ex -exit the credential list")
"""