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


