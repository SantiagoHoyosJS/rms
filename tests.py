import unittest
from typing import List
from inventory.inventario import Inventario, Item
from inventory.pedido import Pedido, PedidoPresencial, PedidoDomicilio
from person.cliente import Cliente
from person.mesa import Mesa, Plato
from core.restaurante import Restaurante

class RestauranteTest (unittest.TestCase):
        
    def test_creacion_restaurante(self)-> None:
        restaurante = Restaurante('Carlos Restaurant')
        self.assertIsNotNone(restaurante)

    def test_creacion_restaurante_forma_2(self)-> None:
        invent = Inventario()
        restaurante = Restaurante('Carlos Restaurant', invent)
        self.assertIsNotNone(restaurante)

    def test_creacion_nombre_restaurante(self) -> None:
        restaurante = Restaurante('Carlos Restaurant')
        self.assertIsNotNone(restaurante.nombre)

    def test_nombre_restaurante(self) -> None:
        nombre = 'Carlos Restaurant'
        restaurante = Restaurante('Carlos Restaurant')
        self.assertEqual(restaurante.nombre, nombre)

    def test_clientes_initial_length_restaurante(self) -> None:
        restaurante = Restaurante('Carlos Restaurant')
        self.assertEqual(len(restaurante.clientes), 0)

    def test_pedidos_initial_length_restaurante(self) -> None:
        restaurante = Restaurante('Carlos Restaurant')
        self.assertEqual(len(restaurante.pedidos), 0)

    def test_mesas_initial_length_restaurante(self) -> None:
        restaurante = Restaurante('Carlos Restaurant')
        self.assertEqual(len(restaurante.mesas), 0)

    def test_platos_initial_length_restaurante(self) -> None:
        restaurante = Restaurante('Carlos Restaurant')
        self.assertEqual(len(restaurante.platos), 0)

    def test_creacion_inventario_restaurante(self) -> None:
        restaurante = Restaurante('Carlos Restaurant')
        invent = Inventario()
        self.assertIsNotNone(restaurante.inventario)

    def test_add_cliente_restaurante(self) -> None:
        restaurante = Restaurante('Carlos Restaurant')
        Lopez = Cliente('Luis') 
        restaurante.add_cliente(Lopez)
        self.assertEqual(len(restaurante.clientes), 1)

    def test_add_pedido_restaurante(self) -> None:
        restaurante = Restaurante('Carlos Restaurant')
        pastas = Plato('Pastas', 'pastas en salsa de tomate', 6000)
        Lopez = Cliente('Luis')
        platos_elejidos = [pastas, pastas]
        pedido = Pedido(Lopez, platos_elejidos)
        restaurante.add_pedido(pedido)
        self.assertEqual(len(restaurante.pedidos), 1)

    def test_add_pedido_presencial_restaurante(self) -> None:
        restaurante = Restaurante('Carlos Restaurant')
        pastas = Plato('Pastas', 'pastas en salsa de tomate', 6000)
        Lopez = Cliente('Luis')
        platos_elejidos = [pastas, pastas]
        mesa = Mesa(1, 4)
        pedido = PedidoPresencial(Lopez, platos_elejidos, mesa)
        restaurante.add_pedido(pedido)
        self.assertEqual(len(restaurante.pedidos), 1)

    def test_add_pedido_domicilio_restaurante(self) -> None:
        restaurante = Restaurante('Carlos Restaurant')
        pastas = Plato('Pastas', 'pastas en salsa de tomate', 6000)
        Lopez = Cliente('Luis')
        platos_elejidos = [pastas, pastas]
        pedido = PedidoDomicilio(Lopez, platos_elejidos, '300000000')
        restaurante.add_pedido(pedido)
        self.assertEqual(len(restaurante.pedidos), 1)

    def test_add_mesa_restaurante(self) -> None:
        restaurante = Restaurante('Carlos Restaurant')
        mesa = Mesa(1, 4) 
        restaurante.add_mesa(mesa)
        self.assertEqual(len(restaurante.mesas), 1)

    def test_remove_mesa_restaurante(self) -> None:
        restaurante = Restaurante('Carlos Restaurant')
        mesa = Mesa(1, 4) 
        restaurante.add_mesa(mesa)
        restaurante.remove_mesa(mesa)
        self.assertEqual(len(restaurante.mesas), 0)

    def test_add_plato_restaurante(self) -> None:
        restaurante = Restaurante('Carlos Restaurant')
        pastas = Plato('Pastas', 'pastas en salsa de tomate', 6000)
        restaurante.add_plato(pastas)
        self.assertEqual(len(restaurante.platos), 1)

    def test_remove_plato_restaurante(self) -> None:
        restaurante = Restaurante('Carlos Restaurant')
        pastas = Plato('Pastas', 'pastas en salsa de tomate', 6000)
        restaurante.add_plato(pastas)
        restaurante.remove_plato(pastas)
        self.assertEqual(len(restaurante.platos), 0)
    
class InventarioTest (unittest.TestCase):
    
    def test_creacion_inventario (self) -> None:
        invent = Inventario()
        self.assertIsNotNone(invent)

    def test_items_initial_length_inventario (self) -> None:
        invent = Inventario()
        self.assertEqual(len(invent.items), 0)

    def test_add_item_inventario(self) -> None:
        invent = Inventario()
        invent.add_item('patata', 1)
        self.assertEqual(len(invent.items), 1)

    def test_add_item_2_inventario(self) -> None:
        invent = Inventario()
        invent.add_item('patata', 1)
        invent.add_item('patata', 3)
        self.assertEqual(len(invent.items), 1)

    def test_add_item_3_inventario(self) -> None:
        invent = Inventario()
        invent.add_item('patata', 1)
        invent.add_item('papa', 2)
        self.assertEqual(len(invent.items), 2)

    def test_quitar_item_inventario(self) -> None:
        invent = Inventario()
        invent.add_item('patata', 1)
        invent.quitar_item(invent.get_item('patata'))
        self.assertEqual(len(invent.items), 0)

    def test_quitar_item_2_inventario(self) -> None:
        invent = Inventario()
        invent.add_item('patata', 1)
        self.assertFalse(invent.quitar_item(invent.get_item('papa')))

    def test_get_item_inventario(self) -> None:
        invent = Inventario()
        invent.add_item('patata', 3)
        self.assertEqual(invent.get_item('patata').cantidad, 3)
    
    def test_get_item_inventario(self) -> None:
        invent = Inventario()
        self.assertFalse(invent.get_item('patata'))

    def test_quitar_cantidad_item_inventario(self) -> None:
        invent = Inventario()
        invent.add_item('patata', 3)
        invent.quitar_cantidad_item(invent.get_item('patata'), 2)
        self.assertEqual(invent.get_item('patata').cantidad, 1)

class ItemTest (unittest.TestCase):

    def test_creacion_item (self) -> None:
        patata = Item('Patata', 1)
        self.assertIsNotNone(patata)

    def test_nombre_item (self) -> None:
        patata = Item('Patata', 1)
        self.assertEqual(patata.nombre, 'Patata')

    def test_cantidad_item (self) -> None:
        patata = Item('Patata', 1)
        self.assertEqual(patata.cantidad, 1)

    # El indice funciona pero como se siguen creando itens antes que este en el main no sabemos cual numero se le asignara como id
    '''def test_id_item (self):
        patata = Item('Patata', 1)
        self.assertEqual(patata.id, 2)'''
    
    def test_aumento_id (self) -> None:
        papa = Item('Papa', 1)
        patata = Item('Patata', 1)
        self.assertEqual(papa.id + 1, patata.id)
    
class ClienteTest (unittest.TestCase):

    def test_creacion_cliente(self) -> None:
        Lopez = Cliente('Luis') 
        self.assertIsNotNone(Lopez)

    def test_nombre_cliente(self) -> None:
        Lopez = Cliente('Luis') 
        self.assertEqual(Lopez.nombre(), 'Luis')

class PLatoTest (unittest.TestCase):

    def test_creacion_plato(self) -> None:
        pastas = Plato('Pastas', 'pastas en salsa de tomate', 6000)
        self.assertIsNotNone(pastas)

    def test_nombre_plato(self) -> None:
        pastas = Plato('Pastas', 'pastas en salsa de tomate', 6000)
        self.assertEqual(pastas.nombre, 'Pastas')

    def test_descripcion_plato(self) -> None:
        pastas = Plato('Pastas', 'pastas en salsa de tomate', 6000)
        self.assertEqual(pastas.descripcion, 'pastas en salsa de tomate')

    def test_precio_plato(self) -> None:
        pastas = Plato('Pastas', 'pastas en salsa de tomate', 6000)
        self.assertEqual(pastas.precio, 6000)

    def test_actualizar_precio_plato(self)  -> None:
        pastas = Plato('Pastas', 'pastas en salsa de tomate', 6000)
        pastas.actualizar_precio(8000)
        self.assertEqual(pastas.precio, 8000)

class MesaTest (unittest.TestCase) :

    def test_creacion_mesa(self) -> None:
        mesa = Mesa(1, 4)
        self.assertIsNotNone(mesa)

    def test_numero_mesa(self) -> None:
        mesa = Mesa(1, 4)
        self.assertEqual(mesa.numero, 1)

    def test_capacidad_mesa(self) -> None:
        mesa = Mesa(1, 4)
        self.assertEqual(mesa.capacidad, 4)

    def test_estado_por_defecto_mesa(self) -> None:
        mesa = Mesa(1, 4)
        self.assertFalse(mesa.ocupada)

    def test_ocupar_mesa(self) -> None:
        mesa = Mesa(1, 4)
        mesa.ocupar()
        self.assertTrue(mesa.ocupada)

    def test_desocupar_mesa(self) -> None:
        mesa = Mesa(1, 4)
        mesa.ocupar()
        mesa.desocupar()
        self.assertFalse(mesa.ocupada)

class PedidoTest (unittest.TestCase):

    def test_creacion_pedido(self) -> None:
        pastas = Plato('Pastas', 'pastas en salsa de tomate', 6000)
        Lopez = Cliente('Luis')
        platos_elejidos = [pastas, pastas]
        pedido = Pedido(Lopez, platos_elejidos)
        self.assertIsNotNone (pedido)

    def test_cliente_pedido(self) -> None:
        pastas = Plato('Pastas', 'pastas en salsa de tomate', 6000)
        Lopez = Cliente('Luis')
        platos_elejidos = [pastas, pastas]
        pedido = Pedido(Lopez, platos_elejidos)
        self.assertEqual(pedido.cliente, Lopez)
    
class PedidoPresencialTest (unittest.TestCase):

    def test_creacion_pedido_Presencial(self) -> None:
        pastas = Plato('Pastas', 'pastas en salsa de tomate', 6000)
        Lopez = Cliente('Luis')
        platos_elejidos = [pastas, pastas]
        mesa = Mesa(1, 4)
        pedido = PedidoPresencial(Lopez, platos_elejidos, mesa)
        self.assertIsNotNone (pedido)

class PedidoDomicilioTest (unittest.TestCase):

    def test_creacion_pedido_domicilio(self) -> None:
        pastas = Plato('Pastas', 'pastas en salsa de tomate', 6000)
        Lopez = Cliente('Luis')
        platos_elejidos = [pastas, pastas]
        pedido = PedidoDomicilio(Lopez, platos_elejidos, '300000000')
        self.assertIsNotNone (pedido)

    