from credentials import Credential

class User():
    user_list =[]
    #Initialize user
    def __init__(self,username,password,credentials:Credential):
        self.username = username
        self.password = password
        self.credentials = credentials

    #Save user method
    def save_user(self):
        User.user_list.append(self)

    #Delete user method
    def delete_user(self):
        User.user_list.remove(self)

    #Check if user exists
    @classmethod
    def user_exists(cls,username):
        for user in cls.user_list:
            if user.username == username:
                return True
        return False

    pass