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

    #Delete Credential
    def delete_credential(self):
        Credential.credential_list.remove(self)

    #Find Credential by account
    @classmethod
    def find_by_account(cls,account):
        for credential in cls.credential_list:
            if credential.account == account:
                return credential

    #Check if credential exists
    @classmethod
    def credential_exist(cls,account):
        for credential in cls.credential_list:
            if credential.account == account:
                return True
        return False

    #Display credentials
    @classmethod
    def display_credentials(cls):
        return cls.credential_list


    pass