from typing import List

from inventory.inventario import Inventario
from inventory.pedido import Pedido
from person.cliente import Cliente
from person.mesa import Mesa, Plato

class Restaurante:
    def __init__(self, nombre, inventario: Inventario = None) -> None:
        self.__nombre = nombre
        self.__clientes: List['Cliente'] = []
        self.__pedidos: List['Pedido'] = []
        self.__mesas: List['Mesa'] = []
        self.__platos: List['Plato'] = [] #Menú
        self.__inventario  = Inventario()

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def clientes(self):
        return self.__clientes
    
    @property
    def pedidos(self):
        return self.__pedidos
    
    @property
    def mesas(self):
        return self.__mesas
    
    @property
    def inventario(self):
        return self.__inventario
    
    @property
    def platos(self):
        return self.__platos    
    
    def add_cliente(self, cliente):
        self.__clientes.append(cliente)

    def add_pedido(self, pedido):
        self.__pedidos.append(pedido)
    
    def add_mesa(self, mesa):
        self.__mesas.append(mesa)
    
    def add_plato(self, plato):
        self.__platos.append(plato)
    
    def remove_plato(self, plato):
        self.__platos.remove(plato)
    
    def add_mesa(self, mesa):
        self.__mesas.append(mesa)
    
    def remove_mesa(self, mesa):
        self.__mesas.remove(mesa)

    
