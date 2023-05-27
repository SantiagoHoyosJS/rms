# from inventory.inventario import Inventario
from interfaces.inicio import inicio 
from interfaces.menu_admin_cliente import menu_admin_cliente
from core.restaurante import Restaurante


def main() -> None:
    restaurante = Restaurante()
    inicio()
    menu_admin_cliente()


    return


if __name__ == '__main__':
    main()