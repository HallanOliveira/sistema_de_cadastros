import os
class BaseController:

    @staticmethod
    def show_message(message):
        print(message)
        input('Digite qualquer tecla para retornar ao menu.')
        os.system('cls')