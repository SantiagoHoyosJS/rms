class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.ocupada = False
    
    def ocupar(self):
        self.ocupada = True
    
    def desocupar(self):
        self.ocupada = False
    
    def __str__(self):
        return f"Mesa {self.numero} ({'ocupada' if self.ocupada else 'desocupada'}) para {self.capacidad} personas"


class Plato:
    def __init__(self, nombre, descripcion='', precio=0):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        self._precio = value

    def __str__(self):
        return f"{self.nombre}: {self.descripcion} - ${self.precio}"
    
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
