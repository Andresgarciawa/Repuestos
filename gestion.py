from tkinter import *
from tkinter import ttk, messagebox
from cliente import Cliente
from repuesto import Repuesto
from orden import Orden

class AplicacionOrdenes:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Órdenes")
        self.root.geometry("800x600")

        # Variables para almacenar datos
        self.ordenes = []
        self.repuestos = []
        self.orden_actual = None

        # Frame principal
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(N, W, E, S))

        # Sección Cliente
        ttk.Label(self.main_frame, text="Datos del Cliente").grid(row=0, column=0, columnspan=2)
        
        ttk.Label(self.main_frame, text="Documento:").grid(row=1, column=0)
        self.doc_cliente = StringVar()
        ttk.Entry(self.main_frame, textvariable=self.doc_cliente).grid(row=1, column=1)

        ttk.Label(self.main_frame, text="Nombre:").grid(row=2, column=0)
        self.nombre_cliente = StringVar()
        ttk.Entry(self.main_frame, textvariable=self.nombre_cliente).grid(row=2, column=1)

        # Sección Orden
        ttk.Label(self.main_frame, text="Datos de la Orden").grid(row=3, column=0, columnspan=2)
        
        ttk.Label(self.main_frame, text="No. Orden:").grid(row=4, column=0)
        self.no_orden = StringVar()
        ttk.Entry(self.main_frame, textvariable=self.no_orden).grid(row=4, column=1)

        ttk.Label(self.main_frame, text="No. Mesa:").grid(row=5, column=0)
        self.no_mesa = StringVar()
        ttk.Entry(self.main_frame, textvariable=self.no_mesa).grid(row=5, column=1)

        # Sección Repuestos
        ttk.Label(self.main_frame, text="Repuestos").grid(row=6, column=0, columnspan=2)
        
        # Lista de repuestos disponibles
        self.repuestos_listbox = Listbox(self.main_frame, height=5)
        self.repuestos_listbox.grid(row=7, column=0, columnspan=2)

        # Botones
        ttk.Button(self.main_frame, text="Crear Orden", command=self.crear_orden).grid(row=8, column=0)
        ttk.Button(self.main_frame, text="Agregar Repuesto", command=self.agregar_repuesto_ventana).grid(row=8, column=1)
        ttk.Button(self.main_frame, text="Mostrar Órdenes", command=self.mostrar_ordenes).grid(row=9, column=0, columnspan=2)

        # Inicializar algunos repuestos de ejemplo
        self.inicializar_repuestos()

    def inicializar_repuestos(self):
        repuestos_iniciales = [
            Repuesto(1, 'Filtro de aire', 50.0),
            Repuesto(2, 'Bujía', 20.0),
            Repuesto(3, 'Aceite de motor', 35.0)
        ]
        for repuesto in repuestos_iniciales:
            self.repuestos.append(repuesto)
            self.repuestos_listbox.insert(END, f"{repuesto.nombre} - ${repuesto.precio}")

    def crear_orden(self):
        try:
            # Crear cliente
            cliente = Cliente(
                self.doc_cliente.get(),
                self.nombre_cliente.get(),
                True
            )

            # Crear orden
            orden = Orden(
                int(self.no_orden.get()),
                int(self.no_mesa.get())
            )
            
            orden.agregarCliente(cliente)
            self.ordenes.append(orden)
            self.orden_actual = orden
            
            messagebox.showinfo("Éxito", "Orden creada correctamente")
            
        except ValueError as e:
            messagebox.showerror("Error", "Por favor ingrese valores válidos")

    def agregar_repuesto_ventana(self):
        if not self.orden_actual:
            messagebox.showerror("Error", "Primero debe crear una orden")
            return

        seleccion = self.repuestos_listbox.curselection()
        if not seleccion:
            messagebox.showerror("Error", "Por favor seleccione un repuesto")
            return

        repuesto = self.repuestos[seleccion[0]]
        self.orden_actual.agregarRepuesto(repuesto)
        messagebox.showinfo("Éxito", f"Repuesto {repuesto.nombre} agregado a la orden")

    def mostrar_ordenes(self):
        if not self.ordenes:
            messagebox.showinfo("Info", "No hay órdenes registradas")
            return

        ventana_ordenes = Toplevel(self.root)
        ventana_ordenes.title("Órdenes Registradas")
        ventana_ordenes.geometry("600x400")

        texto_ordenes = Text(ventana_ordenes, height=20, width=70)
        texto_ordenes.pack(padx=10, pady=10)

        for orden in self.ordenes:
            texto_ordenes.insert(END, orden.mostrarOrden() + "\n\n")

        texto_ordenes.config(state=DISABLED)

def main():
    root = Tk()
    app = AplicacionOrdenes(root)
    root.mainloop()

if __name__ == "__main__":
    main()