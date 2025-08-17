from UserRepository import UserRepository
from UserService import userService

class UserUI:
    def __init__(self, service):
        self.service = service

    def execute (self):
        while True:
            print("\n1. Adicionar usuarios \n2.Listar Usuarios \n3. Sair")
            opcao = input("escolha uma opção")

            if opcao == "1":
                name = input("nome")
                email = input("email")
                try:
                    self.service.createUser(name, email)
                    print("Usuario Cadastrado com sucesso!")
                except ValueError as e:
                    print(f"Error: {e}")
            elif opcao == "2":
                users = self.service.getUsers()
                for user in users:
                    print(f"Nome: {user['nome']}, email: {user['email']}")
            elif opcao == "3":
                break
    
repo = UserRepository()
service = userService(repo)
ui = UserUI(service)
ui.execute()