class Credential:
    #Empty list that holds our credentials
    credential_list = []
    #Define properties for the object credential
    def __init__(self,account,username,email,password):
        self.account = account
        self.username = username
        self.email = email
        self.password = password

    #Save Credential
    def save_credential(self):
        Credential.credential_list.append(self)

    pass