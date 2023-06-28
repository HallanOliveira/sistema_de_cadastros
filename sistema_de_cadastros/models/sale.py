from models.base_model import BaseModel
from models.client import Client
from models.product import Product

class Sale(BaseModel):
    def __init__(self, id_client: str = None, ids_products: str = None, amount_sale: str = None) -> None:
        if ids_products:
            self.products = ids_products.split(',')
        self.client = id_client
        self.amount_sale = amount_sale
        self.DATA_BASE_PATH = '../database_sistema/sales.json'
        super().__init__(self.DATA_BASE_PATH)
        
    def create_sale(self) -> str:
        if(self.validate()):
            self.create({'id_client': self.client,'ids_products': self.products,'amount_sale': self.amount_sale})
            return 'Sucesso - Venda realizada com sucesso!'
        else:
            return 'Erro - Cliente ou produto não existente no banco de dados.'
    
    def get_items(self) -> list:
        data = self.get_data()
        sales = []
        for id, data_sale in data.items():
            client = Client().get_item(data_sale['id_client'])
            sales.append('Venda: ' + id 
                        + '\n  -> Cliente:\n    - ' + client['name'] + ' ' + client['nick_name'] 
                        + '\n  -> Produtos:\n    - ' + '\n    - '.join(Product.get_products_option_by_ids(data_sale['ids_products']))
                        + '\n  -> Total:  ' + data_sale['amount_sale'])

        return len(data), sales
    
    def validate(self) -> bool:
        return bool(Client().validate(self.client) and Product().validate(self.products))