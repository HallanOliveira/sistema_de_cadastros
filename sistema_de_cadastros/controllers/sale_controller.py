from models.product import Product
from models.client import Client
from models.sale import Sale
from views.view_sale import ViewSale
from controllers.base_controller import BaseController
import os

class SaleController(BaseController):

    def create_sale(self):
        os.system('cls')
        print('Selecione 1 cliente (digite o número correspondente):\n')
        id_cliente = int(input('\n'.join(Client().list_options(['name', 'nick_name'])) + '\n'))

        os.system('cls')
        print('Selecione 1 ou mais produtos (separados por vírgula ","):\n')
        ids_products = str(input('\n'.join(Product().list_options(['name', 'price'])) + '\n'))

        os.system('cls')
        amount_sale = str(input('Digite o valor total da venda:\n'))
        response = Sale(id_cliente, ids_products, amount_sale).create_sale()
        self.show_message(response)

    def index(self):
        os.system('cls')
        data = Sale().get_items()
        ViewSale.render(data[0], data[1])
        self.show_message('')