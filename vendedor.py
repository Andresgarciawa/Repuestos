class Vendedor:
    def __init__(self, nombre, ID):
        self.nombre = nombre
        self.ID = ID

    #crear Vendedor
    def crearVendedor(self):
        return f'Vendedor creado: {self.nombre}, Documento: {self.ID},'

    #Mostrar Vendedor
    def mostrarVendedor(self):
        return f'Vendedor: {self.nombre}, Documento: {self.ID},'
    
    #Modificar vendedor
    def modificarVendedor(self, nombre, ID):
        self.nombre = nombre
        self.ID = ID