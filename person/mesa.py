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
    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
    
    def __str__(self):
        return f"{self.nombre}: {self.descripcion} - ${self.precio}"
    
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
