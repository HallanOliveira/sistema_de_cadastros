from models.product import Product
from views.view_product import ViewProduct
from controllers.base_controller import BaseController
import os

class ProductController(BaseController):
    def create_product(self) -> None:
        os.system('cls')
        name = str(input('Digite o nome do produto:\n'))
        price = str(input('Digite o valor do produto:\n'))
        Product(name, price).create_product()
        self.show_message('Sucesso - Produto cadastrado com sucesso!')

    def index(self) -> None:
        os.system('cls')
        data = Product().get_items(['name', 'price'], ': ')
        ViewProduct.render(data[0], data[1])
        self.show_message('')