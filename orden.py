class Orden:
    def __init__(self, noOrden, noMesa):
        self.noOrden = noOrden
        self.noMesa = noMesa
        self.repuestos = []
        self.cliente = None

    def crearOrden(self):
        return f'Orden creada: {self.noOrden}, Mesa: {self.noMesa}'

    def mostrarOrden(self):
        repuestos_str = ', '.join([rep.nombre for rep in self.repuestos])
        cliente_str = self.cliente.mostrarCliente() if self.cliente else 'Sin cliente'
        return f'Orden: {self.noOrden}, Mesa: {self.noMesa}, Cliente: {cliente_str}, Repuestos: {repuestos_str}'

    def agregarRepuesto(self, repuesto):
        self.repuestos.append(repuesto)
        return f'Repuesto agregado: {repuesto.nombre}'

    def quitarRepuesto(self, repuesto):
        self.repuestos.remove(repuesto)
        return f'Repuesto quitado: {repuesto.nombre}'

    def agregarCliente(self, cliente):
        self.cliente = cliente
        return f'Cliente agregado: {cliente.nombre}'
