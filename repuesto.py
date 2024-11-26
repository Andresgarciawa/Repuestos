class Repuesto:
    def __init__(self, id, nombre, cantidad, precio, activo):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.activo = activo

    #crea el repuesto
    def crearRepuesto(self):
        return f'Repuesto creado: {self.nombre}, ID: {self.id}, Cantidad:{self.cantidad}, Precio: {self.precio}, Activo: {self.activo}'

    #muestra el repuesto
    def mostrarRepuesto(self):
        return f'Repuesto: {self.nombre}, ID: {self.id},Cantida{self.cantidad}, Precio: {self.precio}, Activo{self.activo}'
    
    #actualiza el repuesto
    def actualizarRepuesto(self, cantidad, precio, activo):
        self.cantidad = cantidad
        self.precio = precio
        self.activo = activo
        return f'Repuesto actualizado: {self.nombre}, ID: {self.id}, Cantidad: {self.cantidad}, Precio: {self.precio}, Activo{self.activo}'    
    
    #eliminar repuesto
    def eliminarRepuesto(self):
        self.activo = False