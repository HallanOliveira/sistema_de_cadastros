from models.base_model import BaseModel

class Client(BaseModel):
    def __init__(self, name: str = None, nick: str = None) -> None:
        self.__name = name
        self.__nick_name = nick
        self.DATA_BASE_PATH = '../database_sistema/clients.json'
        super().__init__(self.DATA_BASE_PATH)
    
    def create_client(self) -> None:
        self.create({
            'name': self.__name, 
            'nick_name': self.__nick_name
        })
    
    def validate(self, id: str) -> bool:
        try:
            if(self.get_item(id)):
                return True
            else:
                return False
        except:
            return False
