class Vendedor:
    def __init__(self, nombre, ID):
        self.nombre = nombre
        self.ID = ID

    def crearCliente(self):
        return f'Vendedor creado: {self.nombre}, Documento: {self.ID},'

    def mostrarCliente(self):
        return f'Vendedor: {self.nombre}, Documento: {self.ID},'
    