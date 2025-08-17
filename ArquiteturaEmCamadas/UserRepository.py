class UserRepository:
    def __init__(self):
        self.user = []

    def addUser(self, name, email):
        self.user.append({"nome":name, "email":email})

    def listUser(self):
        return self.user

    

    