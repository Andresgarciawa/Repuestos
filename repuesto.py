class Repuesto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    #crea el repuesto
    def crearRepuesto(self):
        return f'Repuesto creado: {self.nombre}, ID: {self.id}, Cantidad:{self.cantidad}, Precio: {self.precio}'

    #muestra el repuesto
    def mostrarRepuesto(self):
        return f'Repuesto: {self.nombre}, ID: {self.id},Cantida{self.cantidad}, Precio: {self.precio}'
    
    #actualiza el repuesto
    def actualizarRepuesto(self, cantidad, precio):
        self.cantidad = cantidad
        self.precio = precio
        return f'Repuesto actualizado: {self.nombre}, ID: {self.id}, Cantidad: {self.cantidad}, Precio: {self.precio}'    
    
    #eliminar repuesto
    def eliminarRepuesto(self):
        self.activo = False
        return f'Repuesto eliminado: {self.nombre}, ID: {self.id}, Cantidad: {self.cantidad}, Precio: {self.precio}'
    
    #modificar repuesto
    def modificarRepuesto(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        return f'Repuesto modificado: {self.nombre}, ID: {self.id}, Cantidad: {self.cantidad}, Precio: {self.precio}'