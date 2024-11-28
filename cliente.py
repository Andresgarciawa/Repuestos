class Cliente:
    def __init__(self, noDocumento, nombre):
        self.noDocumento = noDocumento
        self.nombre = nombre

    def guardar_cliente(self):
        nuevo_cliente = Cliente(self.nombre.get(), self.noDocumento.get())
        self.datoC.append(nuevo_cliente)  # Corrige el nombre de la lista
        self.ventana.destroy()

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
        