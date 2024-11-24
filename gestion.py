from tkinter import *
from tkinter import ttk, messagebox
from cliente import Cliente
from repuesto import Repuesto
from orden import Orden

class VentanaCliente:
    def __init__(self, parent):
        self.ventana = Toplevel(parent)
        self.ventana.title("Registro de Cliente")
        self.ventana.geometry("400x300")
        
        # Frame principal
        main_frame = ttk.Frame(self.ventana, padding="10")
        main_frame.grid(row=0, column=0, sticky=(N, W, E, S))
        
        # Campos del cliente
        ttk.Label(main_frame, text="Registro de Cliente", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(main_frame, text="Documento:").grid(row=1, column=0, pady=5)
        self.doc_cliente = StringVar()
        ttk.Entry(main_frame, textvariable=self.doc_cliente).grid(row=1, column=1, pady=5)
        
        ttk.Label(main_frame, text="Nombre:").grid(row=2, column=0, pady=5)
        self.nombre_cliente = StringVar()
        ttk.Entry(main_frame, textvariable=self.nombre_cliente).grid(row=2, column=1, pady=5)
        
        # Botón de registro
        ttk.Button(main_frame, text="Registrar Cliente", command=self.registrar_cliente).grid(row=3, column=0, columnspan=2, pady=20)
        
    def registrar_cliente(self):
        try:
            cliente = Cliente(self.doc_cliente.get(), self.nombre_cliente.get(), True)
            messagebox.showinfo("Éxito", cliente.crearCliente())
            self.limpiar_campos()
        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar cliente: {str(e)}")
    
    def limpiar_campos(self):
        self.doc_cliente.set("")
        self.nombre_cliente.set("")

class VentanaRepuesto:
    def __init__(self, parent):
        self.ventana = Toplevel(parent)
        self.ventana.title("Registro de Repuesto")
        self.ventana.geometry("400x300")
        
        # Frame principal
        main_frame = ttk.Frame(self.ventana, padding="10")
        main_frame.grid(row=0, column=0, sticky=(N, W, E, S))
        
        # Campos del repuesto
        ttk.Label(main_frame, text="Registro de Repuesto", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(main_frame, text="ID:").grid(row=1, column=0, pady=5)
        self.id_repuesto = StringVar()
        ttk.Entry(main_frame, textvariable=self.id_repuesto).grid(row=1, column=1, pady=5)
        
        ttk.Label(main_frame, text="Nombre:").grid(row=2, column=0, pady=5)
        self.nombre_repuesto = StringVar()
        ttk.Entry(main_frame, textvariable=self.nombre_repuesto).grid(row=2, column=1, pady=5)
        
        ttk.Label(main_frame, text="Precio:").grid(row=3, column=0, pady=5)
        self.precio_repuesto = StringVar()
        ttk.Entry(main_frame, textvariable=self.precio_repuesto).grid(row=3, column=1, pady=5)
        
        # Botón de registro
        ttk.Button(main_frame, text="Registrar Repuesto", command=self.registrar_repuesto).grid(row=4, column=0, columnspan=2, pady=20)
        
    def registrar_repuesto(self):
        try:
            repuesto = Repuesto(
                int(self.id_repuesto.get()),
                self.nombre_repuesto.get(),
                float(self.precio_repuesto.get())
            )
            messagebox.showinfo("Éxito", repuesto.crearRepuesto())
            self.limpiar_campos()
        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar repuesto: {str(e)}")
    
    def limpiar_campos(self):
        self.id_repuesto.set("")
        self.nombre_repuesto.set("")
        self.precio_repuesto.set("")

class MenuPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión")
        self.root.geometry("500x400")
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(N, W, E, S))
        
        # Título
        ttk.Label(
            main_frame, 
            text="Sistema de Gestión de Órdenes",
            font=('Helvetica', 16, 'bold')
        ).grid(row=0, column=0, columnspan=2, pady=20)
        
        # Botones principales
        ttk.Button(
            main_frame,
            text="Registrar Cliente",
            command=self.abrir_registro_cliente,
            width=30
        ).grid(row=1, column=0, columnspan=2, pady=10)
        
        ttk.Button(
            main_frame,
            text="Registrar Repuesto",
            command=self.abrir_registro_repuesto,
            width=30
        ).grid(row=2, column=0, columnspan=2, pady=10)
        
        ttk.Button(
            main_frame,
            text="Gestionar Órdenes",
            command=self.abrir_gestion_ordenes,
            width=30
        ).grid(row=3, column=0, columnspan=2, pady=10)
        
    def abrir_registro_cliente(self):
        VentanaCliente(self.root)
    
    def abrir_registro_repuesto(self):
        VentanaRepuesto(self.root)
    
    def abrir_gestion_ordenes(self):
        AplicacionOrdenes(Toplevel(self.root))

class AplicacionOrdenes:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Órdenes")
        self.root.geometry("800x600")

        # Variables para almacenar datos
        self.ordenes = []
        self.repuestos = []
        self.orden_actual = None

        # Frame principal
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(N, W, E, S))

        # Sección Orden
        ttk.Label(self.main_frame, text="Nueva Orden", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(self.main_frame, text="No. Orden:").grid(row=1, column=0)
        self.no_orden = StringVar()
        ttk.Entry(self.main_frame, textvariable=self.no_orden).grid(row=1, column=1)

        ttk.Label(self.main_frame, text="No. Mesa:").grid(row=2, column=0)
        self.no_mesa = StringVar()
        ttk.Entry(self.main_frame, textvariable=self.no_mesa).grid(row=2, column=1)

        # Botones
        ttk.Button(self.main_frame, text="Crear Orden", command=self.crear_orden).grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Button(self.main_frame, text="Mostrar Órdenes", command=self.mostrar_ordenes).grid(row=4, column=0, columnspan=2)

    def crear_orden(self):
        try:
            orden = Orden(
                int(self.no_orden.get()),
                int(self.no_mesa.get())
            )
            self.ordenes.append(orden)
            self.orden_actual = orden
            messagebox.showinfo("Éxito", "Orden creada correctamente")
        except ValueError as e:
            messagebox.showerror("Error", "Por favor ingrese valores válidos")

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
    app = MenuPrincipal(root)
    root.mainloop()

if __name__ == "__main__":
    main()