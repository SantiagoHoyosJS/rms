from typing import List

class Cliente:
    def __init__(self, nombre) -> None:
        self.__nombre: str = nombre
    
    def get_nombre(self) -> str :
        return self.__nombre