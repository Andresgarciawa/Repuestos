class Cliente:
    def __init__(self, noDocumento, nombre):
        self.noDocumento = noDocumento
        self.nombre = nombre

    #Crear cliente
    def crearCliente(self):
        return f'Cliente creado: {self.nombre}, Documento: {self.noDocumento}'

    #mostrar cliente
    def mostrarCliente(self):
        return f'Cliente: {self.nombre}, Documento: {self.noDocumento}'
    
    #consultar cliente
    def consultarCliente(self):
        return f'Cliente: {self.nombre}, Documento: {self.noDocumento}'
    
    #modificar cliente
    def modificarCliente(self, nombre, noDocumento):
        self.nombre = nombre
        self.noDocumento = noDocumento
        