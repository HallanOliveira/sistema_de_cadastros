from controllers.product_controller import ProductController
from controllers.client_controller import ClientController
from controllers.sale_controller import SaleController
from views.view_menu import ViewMenu
import os

class MenuService:
    """ Menu options """
    """ Client """
    CREATE_CLIENT = 1
    READ_CLIENT = 2
    """ Product """
    CREATE_PRODUCT = 3
    READ_PRODUCT = 4
    """ Sale """
    CREATE_SALE = 5
    READ_SALE = 6
    """ Exit """
    EXIT = 0
    
    def render_menu(self) -> None:
        ViewMenu.render(self.get_options_menu())

    def get_options_menu(self) -> list:
        return [
            str(self.CREATE_CLIENT) + ' - Cadastrar cliente',
            str(self.READ_CLIENT) + ' - Listar clientes',
            str(self.CREATE_PRODUCT) + ' - Cadastrar produto',
            str(self.READ_PRODUCT) + ' - Listar produtos',
            str(self.CREATE_SALE) + ' - Cadastrar venda',
            str(self.READ_SALE) + ' - Listar vendas',
            str(self.EXIT) + ' - Saír',
        ]
    
    def handle_with_option(self) -> bool:
        """ Return None
        Handle with menu option
        """
        match int(input('\nDigite a opção desejada: ')):
            case self.CREATE_CLIENT: ClientController().create_client()
            case self.READ_CLIENT: ClientController().index()

            case self.CREATE_PRODUCT: ProductController().create_product()
            case self.READ_PRODUCT: ProductController().index()
            
            case self.CREATE_SALE: SaleController().create_sale()
            case self.READ_SALE: SaleController().index()
            
            case self.EXIT:
                os.system('cls')
                print('Programa finalizado pelo usuário!')
                return False
            
            case _: print('Opção inválida!')

        return True