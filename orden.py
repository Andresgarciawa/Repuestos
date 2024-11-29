class Orden:
    def __init__(self, noOrden, noMesa, pago):
        self.noOrden = noOrden
        self.noMesa = noMesa
        self.repuestos = []
        self.cliente = None
        self.pago = pago

    def mostrarOrden(self):
        repuestos_str = ', '.join([rep.nombre for rep in self.repuestos])
        cliente_str = self.cliente.mostrarCliente() if self.cliente else 'Sin cliente'
        return f'Orden: {self.noOrden}, Mesa: {self.noMesa}, Cliente: {cliente_str}, Repuestos: {repuestos_str}, Pago: ${self.pago}'

    def agregarRepuesto(self, repuesto):
        self.repuestos.append(repuesto)
        return f'Repuesto agregado: {repuesto.nombre}'

    def quitarRepuesto(self, repuesto):
        if repuesto in self.repuestos:
            self.repuestos.remove(repuesto)
            return f'Repuesto quitado: {repuesto.nombre}'
        else:
            return f'Repuesto {repuesto.nombre} no encontrado en la lista'

    def agregarCliente(self, cliente):
        self.cliente = cliente
        return f'Cliente agregado: {cliente.nombre}'
    
    def agregarpago(self, pago):
        self.pago = pago
        return f'Pago actualizado: {pago}'