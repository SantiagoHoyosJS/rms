from typing import List, Dict

# item = producto

class Item:

    ID = 0

    def __init__(self, nombre: str, cantidad: int) -> None:
        self.__id = Item.ID
        self.__nombre = nombre
        self.__cantidad = cantidad

        Item.ID += 1

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self, value):
        self.__cantidad = value
        return
    
    def __str__(self):
        return f"Item {self.__id}, nombre: {self.__nombre}, cantidad : {self.__cantidad}"
    

class Inventario:
    def __init__(self):
        self.__items: List['Item'] = []

    @property
    def items(self):
        return self.__items

    def add_item(self, nombre_item, cantidad):
        existencia = False
        index = None
        for itemx in self.__items:
            if itemx.nombre == nombre_item:
                existencia = True
                index = self.__items.index(itemx)

        if existencia:
            self.__items[index].cantidad += cantidad
        else:
            new_item = Item(nombre_item, cantidad)
            new_item.cantidad = cantidad
            self.__items.append(new_item)
    
    def quitar_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
            return True
        else:
            return False
        
    def quitar_cantidad_item(self, item, cantidad):
        index = self.__items.index(item)
        if item in self.__items: 
            if self.__items[index].cantidad >= cantidad:
                self.__items[index].cantidad -= cantidad
                if self.__items[index].cantidad == 0:
                    del self.__items[index]
            else:
                print(f"No hay suficiente cantidad de {item.nombre} en el inventario.")
        else:
            print(f"{item.nombre} no está en el inventario.")
            return False
        
    def get_item(self, nombre):
        for i in self.__items:
            if i.nombre == nombre:
                return i
            
    def export(self) -> Dict:
        dic = {}
        for item in self.__items:
            dic[item.id] = [item.nombre, item.cantidad]
        
        return dic

    