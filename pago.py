class Pago:
    def __init__(self, fecha, monto, tipo_pago):
        self.fecha = fecha
        self.monto = monto
        self.tipo_pago = tipo_pago

    #Eliminar pago
    def eliminar_pago(self):
        return "Pago eliminado con éxito"
    
    #pago insuficiente
    def pago_insuficiente(self):
        return "El monto del pago es insuficiente"