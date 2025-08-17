from UserRepository import UserRepository
class userService:
    def __init__(self, repository):
        self.repository = repository

    def createUser(self, name, email):
        if "@" not in email:
            raise ValueError("email invalido!")
        self.repository.addUser(name, email)    

    def getUsers(self):
        return self.repository.listUser()