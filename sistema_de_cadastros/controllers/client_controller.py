from models.client import Client
from views.view_client import ViewClient
from controllers.base_controller import BaseController
import os

class ClientController(BaseController):
    
    def create_client(self) -> None:
        os.system('cls')
        name = str(input('Digite o nome do cliente:\n'))
        nick = str(input('Digite o apelido do cliente:\n'))
        Client(name, nick).create_client()
        self.show_message('Sucesso - Cliente cadastrado com sucesso!')

    def index(self) -> None:
        os.system('cls')
        data = Client().get_items(['name', 'nick_name'], ' ')
        ViewClient.render(data[0], data[1])
        self.show_message('')
