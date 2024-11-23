from repuesto import Repuesto
from cliente import Cliente
from orden import Orden

if __name__ == "__main__":
    # Crear repuestos
    repuesto1 = Repuesto(1, 'Filtro de aire', 50.0)
    repuesto2 = Repuesto(2, 'Bujía', 20.0)

    # Crear cliente
    cliente = Cliente('18421278', 'Wilson Misal', True)

    # Crear orden
    orden = Orden(101, 5)
    orden.agregarCliente(cliente)
    orden.agregarRepuesto(repuesto1)
    orden.agregarRepuesto(repuesto2)

    # Mostrar detalles de la orden
    print(orden.mostrarOrden())
