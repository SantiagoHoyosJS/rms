from typing import List

class Cliente:
    def __init__(self, nombre) -> None:
        self.__nombre: str = nombre
        self.__telefono: str = ''
        self.__email: str = ''


    @property
    def nombre(self):
        return self.__nombre
    