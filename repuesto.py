class Repuesto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    def crearRepuesto(self):
        return f'Repuesto creado: {self.nombre}, ID: {self.id}, Precio: {self.precio}'
