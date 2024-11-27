from tkinter import *
from tkinter import ttk, messagebox
from cliente import Cliente
from repuesto import Repuesto
from orden import Orden
from pago import Pago

# [Las clases VentanaCliente y VentanaRepuesto se mantienen igual]

class MenuPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión")
        self.root.geometry("700x500")
        
        # Listas para almacenar clientes y repuestos
       # self.vendedor = []
        self.clientes = []
        self.repuestos = []
        self.ordenes = []
        self.pagos = []
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(N, W, E, S))
        
        # Título
        ttk.Label(
            main_frame, 
            text="Sistema de Gestión de Órdenes",
            font=('Helvetica', 16, 'bold')
        ).grid(row=0, column=0, columnspan=2, pady=20)
        
        # Cargar imágenes 
        self.img_vendedor = PhotoImage(file="iconos/vendedor.png")
        self.img_cliente = PhotoImage(file="iconos/cliente.png") 
        self.img_repuesto = PhotoImage(file="iconos/repuesto.png")
        self.img_orden = PhotoImage(file="iconos/orden.png")
        
        # Botón Registrar vendedor con imagen
        ttk.Button(
            main_frame,
            text="Registrar Vendedor",
            image=self.img_vendedor,  # Agrega la imagen
           compound=LEFT,  # Coloca la imagen a la izquierda del texto
            #command=self.abrir_registro_vendedor,
            width=30
       ).grid(row=1, column=0, columnspan=2, pady=10)

        # Botón Registrar Cliente con imagen
        ttk.Button(
            main_frame,
            text="Registrar Cliente",
            image=self.img_cliente,  # Agrega la imagen
            compound=LEFT,  # Coloca la imagen a la izquierda del texto
            command=self.abrir_registro_cliente,
            width=30
        ).grid(row=1, column=2, columnspan=2, pady=10)
        
        # Botón Registrar Repuesto con imagen
        ttk.Button(
            main_frame,
            text="Registrar Repuesto",
            image=self.img_repuesto,
            compound=LEFT,
            command=self.abrir_registro_repuesto,
            width=30
        ).grid(row=2, column=0, columnspan=2, pady=10)
        
        # Botón Gestionar Órdenes con imagen
        ttk.Button(
            main_frame,
            text="Gestionar Órdenes",
            image=self.img_orden,
            compound=LEFT,
            command=self.abrir_gestion_ordenes,
            width=30
        ).grid(row=2, column=2, columnspan=2, pady=10)

        # Etiqueta de versión con un estilo más discreto
        ttk.Label(
            main_frame, 
            text="v1.0.0 | © 2024",
            font=('Helvetica', 8),
            # Color gris
            foreground='gray'  
        ).grid(row=3, column=0, columnspan=2, pady=10)
    
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
    
    def agregar_repuesto(self, repuesto):
        self.repuestos.append(repuesto)

    def agregar_pago(self):
        self.orden.append()
        
    def abrir_registro_cliente(self):
        VentanaCliente(self.root)
    
    def abrir_registro_repuesto(self):
        VentanaRepuesto(self.root)
    
    def abrir_gestion_ordenes(self):
        AplicacionOrdenes(Toplevel(self.root), self.clientes, self.repuestos)

    def agregar_pago(self, pago):
        self.orden.append(pago)

class VentanaCliente:
    def __init__(self, root):
        self.ventana = Toplevel(root)
        self.ventana.title("Registro de Cliente")
        self.ventana.geometry("400x300")
        
        # Implementa aquí los campos para registrar un cliente
        ttk.Label(self.ventana, text="Nombre:").grid(row=0, column=0)
        self.nombre = StringVar()
        ttk.Entry(self.ventana, textvariable=self.nombre).grid(row=0, column=1)
        
        ttk.Label(self.ventana, text="No. Documento:").grid(row=1, column=0)
        self.noDocumento = StringVar()
        ttk.Entry(self.ventana, textvariable=self.noDocumento).grid(row=1, column=1)
        
        # Botón para guardar cliente
        ttk.Button(self.ventana, text="Guardar", command=self.guardar_cliente).grid(row=2, column=0, columnspan=2)
    
    def guardar_cliente(self):
        # Aquí debes crear un nuevo objeto Cliente y agregarlo a la lista de clientes
        nuevo_cliente = Cliente(self.nombre.get(), self.noDocumento.get())
        # Asumiendo que tienes acceso al MenuPrincipal para agregar el cliente
        # Necesitarás pasar una referencia al MenuPrincipal o usar un método de clase
        self.ventana.destroy()

class VentanaRepuesto:
    def __init__(self, root):
        self.ventana = Toplevel(root)
        self.ventana.title("Registro de Repuesto")
        self.ventana.geometry("400x300")
        
        # Implementa aquí los campos para registrar un repuesto
        ttk.Label(self.ventana, text="Nombre:").grid(row=0, column=0)
        self.nombre = StringVar()
        ttk.Entry(self.ventana, textvariable=self.nombre).grid(row=0, column=1)

        #Id del producto
        ttk.Label(self.ventana, text="ID:").grid(row=1, column=0)
        self.id = StringVar()
        ttk.Entry(self.ventana, textvariable=self.id).grid(row=1, column=1)

        #cantidad de producto
        ttk.Label(self.ventana, text="Cantidad:").grid(row=2, column=0)
        self.cantidad = StringVar()
        ttk.Entry(self.ventana, textvariable=self.cantidad).grid(row=2, column=1)

        #precio del producto
        ttk.Label(self.ventana, text="Precio:").grid(row=2, column=0)
        self.precio = StringVar()
        ttk.Entry(self.ventana, textvariable=self.precio).grid(row=2, column=1)

        #activacion de producto
        ttk.Label(self.ventana, text="Activado:").grid(row=3, column=0)
        self.activado = StringVar()
        ttk.Checkbutton(self.ventana, variable=self.activado).grid(row=3, column=1)
        
        #inactivacion de producto
        ttk.Label(self.ventana, text="Inactivo:").grid(row=4, column=0)
        self.inactivo = StringVar()
        ttk.Checkbutton(self.ventana, variable=self.inactivo).grid(row=4, column=1)

        #solo debe estar activo un checkbutton si esta activo uno desmarca el otro
        self.activado.set(True)
        self.inactivo.set(False)
        
        # Botón para guardar repuesto
        ttk.Button(self.ventana, text="Guardar", command=self.guardar_repuesto).grid(row=5, column=0, columnspan=2)

    def guardar_repuesto(self):
        # Aquí debes crear un nuevo objeto Repuesto y agregarlo a la lista de repuestos
        nuevo_repuesto = Repuesto(int(self.id.get()), self.nombre.get(), float(self.precio.get()), float(self.cantidad.get), self.activo.get())
        # Necesitarás modificar el código para agregar el repuesto
        self.ventana.destroy()   

    def actualizarRepuesto(self):
        # Se acualiza el repuesto
        self.id.set("1")
        self.nombre.set("Repuesto 1")
        self.precio.set("10.0")
        self.cantidad,set("10")

class VentanaVendedor:
    def __init__(self, root):
        self.ventana = Toplevel(root)
        self.ventana.title("Registro de Repuesto")
        self.ventana.geometry("400x300")
        
        # Implementa aquí los campos para registrar un repuesto
        ttk.Label(self.ventana, text="Nombre:").grid(row=0, column=0)
        self.nombre = StringVar()
        ttk.Entry(self.ventana, textvariable=self.nombre).grid(row=0, column=1)
        
        ttk.Label(self.ventana, text="ID:").grid(row=1, column=0)
        self.id = StringVar()
        ttk.Entry(self.ventana, textvariable=self.id).grid(row=1, column=1)
        
        ttk.Label(self.ventana, text="Precio:").grid(row=2, column=0)
        self.precio = StringVar()
        ttk.Entry(self.ventana, textvariable=self.precio).grid(row=2, column=1)
        
        # Botón para guardar repuesto
        ttk.Button(self.ventana, text="Guardar", command=self.guardar_repuesto).grid(row=3, column=0, columnspan=2)

class AplicacionOrdenes:
    def __init__(self, root, clientes, repuestos):
        self.root = root
        self.root.title("Gestión de Órdenes")
        self.root.geometry("800x600")

        # Variables para almacenar datos
        self.clientes = clientes
        self.repuestos = repuestos
        self.ordenes = []
        self.orden_actual = None
        self.cliente_actual = None
        self.repuestos_seleccionados = []

        # Frame principal
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(N, W, E, S))

        # Título
        ttk.Label(self.main_frame, text="Nueva Orden", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Sección Orden
        ttk.Label(self.main_frame, text="No. Orden:").grid(row=1, column=0)
        self.no_orden = StringVar()
        ttk.Entry(self.main_frame, textvariable=self.no_orden).grid(row=1, column=1)

        ttk.Label(self.main_frame, text="No. Mesa:").grid(row=2, column=0)
        self.no_mesa = StringVar()
        ttk.Entry(self.main_frame, textvariable=self.no_mesa).grid(row=2, column=1)

        # Sección Cliente
        ttk.Label(self.main_frame, text="Buscar Cliente", font=('Helvetica', 10, 'bold')).grid(row=3, column=0, columnspan=2, pady=10)
        
        ttk.Label(self.main_frame, text="Documento Cliente:").grid(row=4, column=0)
        self.doc_cliente_buscar = StringVar()
        ttk.Entry(self.main_frame, textvariable=self.doc_cliente_buscar).grid(row=4, column=1)
        ttk.Button(self.main_frame, text="Buscar Cliente", command=self.buscar_cliente).grid(row=4, column=2)

        # Información del cliente
        self.info_cliente = StringVar()
        ttk.Label(self.main_frame, textvariable=self.info_cliente).grid(row=5, column=0, columnspan=3, pady=5)

        # Sección Repuestos
        ttk.Label(self.main_frame, text="Agregar Repuestos", font=('Helvetica', 10, 'bold')).grid(row=6, column=0, columnspan=2, pady=10)
        
        ttk.Label(self.main_frame, text="ID Repuesto:").grid(row=7, column=0)
        self.id_repuesto_buscar = StringVar()
        ttk.Entry(self.main_frame, textvariable=self.id_repuesto_buscar).grid(row=7, column=1)
        ttk.Button(self.main_frame, text="Agregar Repuesto", command=self.agregar_repuesto).grid(row=7, column=2)

        # Lista de repuestos seleccionados
        ttk.Label(self.main_frame, text="Repuestos Seleccionados:").grid(row=8, column=0, columnspan=3, pady=5)
        self.lista_repuestos = Listbox(self.main_frame, height=5, width=50)
        self.lista_repuestos.grid(row=9, column=0, columnspan=3, pady=5)

        #Ingresar pago
        ttk.Label(self.main_frame, text="Ingresar Pago").grid(row=10, column=0, columnspan=2, pady=10)
        self.pago = StringVar()
        ttk.Entry(self.main_frame, textvariable=self.pago).grid(row=10, column=1, columnspan=2, pady=10)
                                                                

        # Botones
        ttk.Button(self.main_frame, text="Crear Orden", command=self.crear_orden).grid(row=11, column=0, pady=10)
        ttk.Button(self.main_frame, text="Mostrar Órdenes", command=self.mostrar_ordenes).grid(row=11, column=1)

    def buscar_cliente(self):
        documento = self.doc_cliente_buscar.get()
        cliente_encontrado = None
        
        # Buscar en la lista de clientes
        for cliente in self.clientes:
            if cliente.noDocumento == documento:
                cliente_encontrado = cliente
                break
        
        if cliente_encontrado:
            self.cliente_actual = cliente_encontrado
            self.info_cliente.set(f"Cliente encontrado: {cliente_encontrado.nombre}")
        else:
            messagebox.showerror("Error", "Cliente no encontrado")
            self.cliente_actual = None
            self.info_cliente.set("Cliente no encontrado")

    def agregar_repuesto(self):
        try:
            id_repuesto = int(self.id_repuesto_buscar.get())
            repuesto_encontrado = None
            
            # Buscar en la lista de repuestos
            for repuesto in self.repuestos:
                if repuesto.id == id_repuesto:
                    repuesto_encontrado = repuesto
                    break
            
            if repuesto_encontrado:
                self.repuestos_seleccionados.append(repuesto_encontrado)
                self.lista_repuestos.insert(END, f"{repuesto_encontrado.nombre} - ${repuesto_encontrado.precio}")
                self.id_repuesto_buscar.set("")
            else:
                messagebox.showerror("Error", "Repuesto no encontrado")
        except ValueError:
            messagebox.showerror("Error", "ID de repuesto inválido")

    def agregar_pago(self):
        try:
            monto = float(self.monto_pago.get())
            self.pagos.append(monto)
            self.lista_pagos.insert(END, f"Pago de ${monto}")
            self.monto_pago.set("")
        except ValueError:
            messagebox.showerror("Error", "Monto de pago inválido")

    def crear_orden(self):
        if not self.cliente_actual:
            messagebox.showerror("Error", "Debe seleccionar un cliente")
            return
            
        if not self.repuestos_seleccionados:
            messagebox.showerror("Error", "Debe agregar al menos un repuesto")
            return
            
        try:
            # Crear la orden
            orden = Orden(
                int(self.no_orden.get()),
                int(self.no_mesa.get())
            )
            
            # Agregar cliente y repuestos
            orden.agregarCliente(self.cliente_actual)
            for repuesto in self.repuestos_seleccionados:
                orden.agregarRepuesto(repuesto)
            
            self.ordenes.append(orden)
            messagebox.showinfo("Éxito", "Orden creada correctamente")
            
            # Limpiar campos
            self.limpiar_campos()
            
        except ValueError as e:
            messagebox.showerror("Error", "Por favor ingrese valores válidos")

    def limpiar_campos(self):
        self.no_orden.set("")
        self.no_mesa.set("")
        self.doc_cliente_buscar.set("")
        self.id_repuesto_buscar.set("")
        self.info_cliente.set("")
        self.lista_repuestos.delete(0, END)
        self.cliente_actual = None
        self.repuestos_seleccionados = []

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