from abc import ABC
from typing import List

from person.cliente import Cliente
from person.mesa import Mesa, Plato

class Pedido(ABC):
    ID = 1

    def __init__(self, cliente, platos: List['Plato']) -> None:
        self.__id: Pedido.ID
        self.__cliente: Cliente = cliente
        self.__platos: List['Plato'] = platos

        Pedido.ID += 1

    def get_cliente(self) -> 'Cliente':
        return self.__cliente
    
    def get_platos(self) -> list['Plato']:
        return self.__platos
    

class PedidoPresencial(Pedido):
    def __init__(self, cliente, platos: List['Plato'], mesa: Mesa) -> None:
        super().__init__(cliente, platos)
        self.__mesa: Mesa = mesa

class PedidoDomicilio(Pedido):
    def __init__(self, cliente, platos: List['Plato'], telefono: str) -> None:
        super().__init__(cliente, platos)
        self.__telefono: str = telefono