from credentials import Credential

class User():
    def __init__(self,username,password,credentials:Credential):
        self.username = username
        self.password = password
        self.credentials = credentials

    pass