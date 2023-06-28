from models.base_model import BaseModel

class Product(BaseModel):

    def __init__(self, name: str = None, price: float = None) -> None:
        self.name = name
        self.price = price
        self.DATA_BASE_PATH = '../database_sistema/products.json'
        super().__init__(self.DATA_BASE_PATH)
    
    def create_product(self) -> None:
        self.create({
            'name': self.name, 
            'price': self.price
        })
    
    def validate(self, ids) -> bool:
        if(ids):
            for i in ids:
                try:
                    if(self.get_item(i)):
                        continue
                    else:
                        return False
                except:
                    return False
            return True
        else:
            return False
    
    @staticmethod
    def get_products_option_by_ids(ids: list | str) -> list:
        products = []
        for id in ids:
            item = Product().get_item(id)
            products.append(item['name'] + ': ' + item['price'])
        return products