class Cliente:
    def __init__(self, noDocumento, nombre, estado):
        self.noDocumento = noDocumento
        self.nombre = nombre
        self.estado = estado

    def crearCliente(self):
        return f'Cliente creado: {self.nombre}, Documento: {self.noDocumento}, Estado: {self.estado}'

    def mostrarCliente(self):
        return f'Cliente: {self.nombre}, Documento: {self.noDocumento}, Estado: {self.estado}'
