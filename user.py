from credentials import Credential

class User():
    user_list =[]
    def __init__(self,username,password,credentials:Credential):
        self.username = username
        self.password = password
        self.credentials = credentials

    pass