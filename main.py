from inventory.inventario import Inventario

def main() -> None:
    inventario = Inventario()
    for i in range(10):
        inventario.add_item('pera', 2)
    print(inventario.items[0])
    inventario.quitar_cantidad_item(inventario.get_item('pera'), 2)
    print(inventario.items[0])
    print(inventario.export())
    inventario.quitar_item(inventario.get_item('pera'))
    print(inventario.items)



    return


if __name__ == '__main__':
    main()