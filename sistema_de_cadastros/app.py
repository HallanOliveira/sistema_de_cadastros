from services.menu_service import MenuService
import os

menu = MenuService()
run = True

os.system('cls')

while run:
    try:
        menu.render_menu()
        run = menu.handle_with_option()
    except Exception as error:
        run = False
        print(error)