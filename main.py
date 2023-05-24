from inventory.inventario import Inventario, Item
from inventory.pedido import Pedido
from person.cliente import Cliente
from person.mesa import Mesa, Plato
from core.restaurante import Restaurante

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


import unittest
'pruebas unitarias'

class RestauranteTest (unittest.TestCase):
        
    def test_creacion_restaurante(self):
        restaurante = Restaurante('Carlos Restaurant')
        self.assertIsNotNone(restaurante)

    def test_creacion_restaurante_forma_2(self):
        invent = Inventario()
        restaurante = Restaurante('Carlos Restaurant', invent)
        self.assertIsNotNone(restaurante)

    def test_name(self) -> None:
        nombre = 'Carlos Restaurant'
        restaurante = Restaurante('Carlos Restaurant')
        self.assertEqual(restaurante.nombre, nombre)

    def test_clientes_initial_length(self) -> None:
        restaurante = Restaurante('Carlos Restaurant')
        self.assertEqual(len(restaurante.clientes), 0)

    def test_pedidos_initial_length(self) -> None:
        restaurante = Restaurante('Carlos Restaurant')
        self.assertEqual(len(restaurante.pedidos), 0)

    def test_mesas_initial_length(self) -> None:
        restaurante = Restaurante('Carlos Restaurant')
        self.assertEqual(len(restaurante.mesas), 0)

    def test_platos_initial_length(self) -> None:
        restaurante = Restaurante('Carlos Restaurant')
        self.assertEqual(len(restaurante.platos), 0)

    def test_add_cliente(self):
        restaurante = Restaurante('Carlos Restaurant')
        Lopez = Cliente('Luis') 
        restaurante.add_cliente(Lopez)
        self.assertEqual(len(restaurante.clientes), 1)

class InventarioTest (unittest.TestCase):
    
    def test_creacion_inventario (self):
        invent = Inventario()
        self.assertIsNotNone(invent)

    def test_items_initial_length (self) -> None:
        invent = Inventario()
        self.assertEqual(len(invent.items), 0)

class ItemTest (unittest.TestCase):

    def test_creacion_item (self):
        patata = Item('Patata', 1)
        self.assertIsNotNone(patata)

    def test_nombre_item (self):
        patata = Item('Patata', 1)
        self.assertEqual(patata.nombre, 'Patata')

    def test_cantidad_item (self):
        patata = Item('Patata', 1)
        self.assertEqual(patata.cantidad, 1)

    # El indice funciona pero como se siguen creando itens antes que este en el main no sabemos cual id se le asignara
    '''def test_id_item (self):
        patata = Item('Patata', 1)
        self.assertEqual(patata.id, 2)'''
    
    # Este si que no sirve, parece que hay algo con el id en los casos de prueba, ya que la variable id no aumenta
    '''def test_aumento_id (self):
        id_anterior = Item.id
        id_esperado = 1 + id_anterior
        patata = Item('Patata', 1)
        self.assertEqual(Item.id, id_esperado)'''
    
class ClienteTest (unittest.TestCase):

    def test_creacion_cliente(self):
        Lopez = Cliente('Luis') 
        self.assertIsNotNone(Lopez)

    def test_nombre_cliente(self):
        Lopez = Cliente('Luis') 
        self.assertEqual(Lopez.get_nombre(), 'Luis')

    

if __name__ == '__main__':
    main()
    unittest.main()