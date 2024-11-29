from tkinter import *
from tkinter import ttk, messagebox, Toplevel, StringVar, Listbox, Text, END, N, W, E, S
from cliente import Cliente
from repuesto import Repuesto
from orden import Orden
import os
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# [Las clases VentanaCliente y VentanaRepuesto se mantienen igual]

class MenuPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión")
        self.root.geometry("700x500")
        
        # Listas para almacenar clientes y repuestos
        self.clientes = []  # Se pasa como datoC en VentanaCliente
        self.repuestos = []  # Se pasa como datoR en VentanaRepuesto
        self.vendedor = []
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
        self.img_soporte = PhotoImage(file="iconos/soporte.png")
        self.img_reporte = PhotoImage(file="iconos/reporte.png")
        
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

        # Botón Soporte
        ttk.Button(
            main_frame,
            text="Soporte",
            image=self.img_soporte,
            compound=LEFT,
            command=self.abrir_soporte,
            width=30
        ).grid(row=3, column=0, columnspan=2, pady=10)

        # Botón Reportes
        ttk.Button(
            main_frame,
            text="Reportes",
            image=self.img_reporte,
            compound=LEFT,
            command=self.abrir_reportes,
            width=30
        ).grid(row=3, column=2, columnspan=2, pady=10)

        # Etiqueta de versión con un estilo más discreto
        ttk.Label(
            main_frame, 
            text="v1.0.6 | © 2024",
            font=('Helvetica', 8),
            # Color gris
            foreground='gray'  
        ).grid(row=4, column=0, columnspan=2, pady=10)
    
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
    
    def agregar_repuesto(self, repuesto):
        self.repuestos.append(repuesto)

    def agregar_pago(self):
        self.orden.append()
        
    def abrir_registro_cliente(self):
        VentanaCliente(self.root, self.clientes)
    
    def abrir_registro_repuesto(self):
        VentanaRepuesto(self.root, self.repuestos)
        
    def abrir_gestion_ordenes(self):
        AplicacionOrdenes(Toplevel(self.root), self.clientes, self.repuestos)

    def agregar_pago(self, pago):
        self.orden.append(pago)
    
    def abrir_reportes(self):
        VentanaReporte(self.root)

    def abrir_soporte(self):
        VentanaSoporte(self.root)


class Cliente:
    def __init__(self, nombre, no_documento):
        self.nombre = nombre
        self.no_documento = no_documento

    def __repr__(self):
        return f"{self.nombre} (Documento: {self.no_documento})"

class VentanaCliente:
    def __init__(self, root, datoC):
        self.datoC = datoC  # Recibe la lista de clientes
        self.ventana = Toplevel(root)
        self.ventana.title("Registro de Cliente")
        self.ventana.geometry("400x300")
        
        # Campos para registrar un cliente
        ttk.Label(self.ventana, text="Nombre:").grid(row=0, column=0)
        self.nombre = StringVar()
        ttk.Entry(self.ventana, textvariable=self.nombre).grid(row=0, column=1)
        
        ttk.Label(self.ventana, text="No. Documento:").grid(row=1, column=0)
        self.noDocumento = StringVar()
        ttk.Entry(self.ventana, textvariable=self.noDocumento).grid(row=1, column=1)
        
        # Botón para guardar cliente
        ttk.Button(self.ventana, text="Guardar", command=self.guardar_cliente).grid(row=2, column=0, columnspan=2)
    
    def guardar_cliente(self):
        # Crear un nuevo cliente con los datos ingresados
        nuevo_cliente = Cliente(self.nombre.get(), self.noDocumento.get())
        self.datoC.append(nuevo_cliente)  # Agregar el nuevo cliente a la lista
        messagebox.showinfo("Éxito", "Cliente registrado exitosamente")
        self.ventana.destroy()  # Cerrar la ventana después de guardar

    def limpiar_campos(self):
        # Limpiar cliente
        self.nombre.set("")
        self.noDocumento.set("")

class VentanaRepuesto:
    def __init__(self, root, datoR):
        self.datoRepuesto = datoR  # Recibe la lista de repuestos
        self.ventana = Toplevel(root)
        self.ventana.title("Registro de Repuesto")
        self.ventana.geometry("400x300")
        
        # Campos para registrar un repuesto
        ttk.Label(self.ventana, text="Nombre:").grid(row=0, column=0)
        self.nombre = StringVar()
        ttk.Entry(self.ventana, textvariable=self.nombre).grid(row=0, column=1)

        ttk.Label(self.ventana, text="ID:").grid(row=1, column=0)
        self.id = StringVar()
        ttk.Entry(self.ventana, textvariable=self.id).grid(row=1, column=1)

        ttk.Label(self.ventana, text="Precio:").grid(row=2, column=0)
        self.precio = StringVar()
        ttk.Entry(self.ventana, textvariable=self.precio).grid(row=2, column=1)

        ttk.Label(self.ventana, text="Cantidad:").grid(row=3, column=0)
        self.cantidad = StringVar()
        ttk.Entry(self.ventana, textvariable=self.cantidad).grid(row=3, column=1)
        
        # Botón para guardar repuesto
        ttk.Button(self.ventana, text="Guardar", command=self.guardar_repuesto).grid(row=4, column=0, columnspan=2)

    def guardar_repuesto(self):
        try:
            # Crear el nuevo repuesto con los datos ingresados
            nuevo_repuesto = Repuesto(
                int(self.id.get()),
                self.nombre.get(),
                float(self.precio.get()),
                int(self.cantidad.get())
            )
            # Agregar el nuevo repuesto a la lista
            self.datoRepuesto.append(nuevo_repuesto)
            messagebox.showinfo("Éxito", "Repuesto registrado exitosamente")
            self.ventana.destroy()  # Cerrar la ventana de repuestos
        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")

    def actualizar_repuesto(self):
        # Este método puede actualizar los campos con valores predefinidos si deseas
        self.id.set("1")
        self.nombre.set("Repuesto 1")
        self.precio.set("10.0")
        self.cantidad.set("10")

    def limpiar_campos(self):
        # Limpiar Repuesto
        self.id.set("")
        self.nombre.set("")
        self.precio.set("")
        self.cantidad.set("")

class VentanaVendedor:
    def __init__(self, root): #se crea la clase de la ventana del vendedor 
        self.ventana = Toplevel(root)
        self.ventana.title("Registro de Repuesto")
        self.ventana.geometry("400x300")
        
        # Implementa aquí los campos para registrar al vendedor
        ttk.Label(self.ventana, text="Nombre:").grid(row=0, column=0)
        self.nombre = StringVar()
        ttk.Entry(self.ventana, textvariable=self.nombre).grid(row=0, column=1)
        # se implementan los campos para registrar el ID del vendendor
        ttk.Label(self.ventana, text="ID:").grid(row=1, column=0)
        self.id = StringVar()
        ttk.Entry(self.ventana, textvariable=self.id).grid(row=1, column=1)

    def limpiar_campos(self):
        # Limpiar Vendedor
        self.nombre.set("")
        self.id.set("")


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
        self.pagos = []

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

        # Sección de Pago
        ttk.Label(self.main_frame, text="Pago", font=('Helvetica', 10, 'bold')).grid(row=10, column=0, columnspan=2, pady=10)

        ttk.Label(self.main_frame, text="Monto Pagado:").grid(row=11, column=0)
        self.monto_pagado = StringVar()
        ttk.Entry(self.main_frame, textvariable=self.monto_pagado).grid(row=11, column=1)

        # Botones
        ttk.Button(self.main_frame, text="Crear Orden", command=self.crear_orden).grid(row=12, column=0, pady=10)
        ttk.Button(self.main_frame, text="Mostrar Órdenes", command=self.mostrar_ordenes).grid(row=12, column=1)

    def buscar_cliente(self):
        documento = self.doc_cliente_buscar.get()
        cliente_encontrado = None

        for cliente in self.clientes:
            if cliente.no_documento == documento:
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

    def crear_orden(self):
        # Validar que el cliente esté seleccionado
        if not self.cliente_actual:
            messagebox.showerror("Error", "Debe seleccionar un cliente")
            return

        # Validar que se hayan agregado repuestos
        if not self.repuestos_seleccionados:
            messagebox.showerror("Error", "Debe agregar al menos un repuesto")
            return

        try:
            # Validar y convertir los valores de no_orden y no_mesa
            no_orden = int(self.no_orden.get())
            no_mesa = int(self.no_mesa.get())
        except ValueError:
            messagebox.showerror("Error", "Los números de orden y mesa deben ser valores numéricos válidos")
            return

        # Verificar que el número de orden no esté duplicado
        if any(orden.noOrden == no_orden for orden in self.ordenes):
            messagebox.showerror("Error", "El número de orden ya existe")
            return

        try:
            # Calcular el total de la orden y validar el monto de pago
            total = sum([repuesto.precio for repuesto in self.repuestos_seleccionados])
            pago = float(self.monto_pagado.get())

            if pago < total:
                messagebox.showerror("Error", f"El monto pagado ({pago}) es insuficiente. Total a pagar: {total}")
                return

            # Crear la orden
            orden = Orden(no_orden, no_mesa, pago)
            orden.agregarCliente(self.cliente_actual)

            for repuesto in self.repuestos_seleccionados:
                orden.agregarRepuesto(repuesto)

            # Registrar el pago
            self.ordenes.append(orden)
            self.cliente_actual = None
            self.repuestos_seleccionados = []
            self.no_orden.set("")
            self.no_mesa.set("")
            self.monto_pagado.set("")

            # Mostrar mensaje de éxito y limpiar los campos
            messagebox.showinfo("Éxito", "Orden creada correctamente")
            self.limpiar_campos()

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos para el pago")

    def mostrar_ordenes(self):
        """Muestra una lista de órdenes creadas en una ventana secundaria."""
        if not self.ordenes:
            messagebox.showinfo("Sin Órdenes", "No hay órdenes registradas")
            return

        # Crear una ventana secundaria
        ventana_ordenes = Toplevel(self.root)
        ventana_ordenes.title("Lista de Órdenes")
        ventana_ordenes.geometry("600x400")

        # Título
        ttk.Label(ventana_ordenes, text="Órdenes Registradas", font=('Helvetica', 12, 'bold')).pack(pady=10)

        # Crear una lista para mostrar las órdenes
        lista_ordenes = Listbox(ventana_ordenes, width=80, height=20)
        lista_ordenes.pack(pady=10)

        # Insertar datos de cada orden en la lista
        for orden in self.ordenes:
            lista_ordenes.insert(END, f"No. Orden: {orden.noOrden} | Mesa: {orden.noMesa} | Pago: ${orden.pago:.2f}")
            lista_ordenes.insert(END, f"Cliente: {orden.cliente.nombre} ({orden.cliente.no_documento})")
            repuestos = ", ".join(f"{r.nombre} (${r.precio:.2f})" for r in orden.repuestos)
            lista_ordenes.insert(END, f"Repuestos: {repuestos}")
            lista_ordenes.insert(END, "-" * 60)



    def limpiar_campos(self):
        # Limpiar cliente
        self.cliente_actual = None
        self.info_cliente.set("Cliente no seleccionado")

        # Limpiar repuestos seleccionados
        self.repuestos_seleccionados = []
        self.lista_repuestos.delete(0, END)

        # Limpiar entradas de texto
        self.no_orden.set("")
        self.no_mesa.set("")
        self.monto_pagado.set("")
        self.id_repuesto_buscar.set("")
        self.doc_cliente_buscar.set("")



# Clase Ventana Soporte
class VentanaSoporte:
    def __init__(self, root):
        self.ventana = Toplevel(root)
        self.ventana.title("Soporte")
        self.ventana.geometry("400x200")

        ttk.Label(self.ventana, text="Correo de Soporte:").grid(row=0, column=0)
        ttk.Label(self.ventana, text="soporte@gmail.com").grid(row=1, column=0)
        ttk.Label(self.ventana, text="Personas de contacto:").grid(row=2, column=0)
        ttk.Label(self.ventana, text="Wilson Andres Garcia").grid(row=3, column=0)
        ttk.Label(self.ventana, text="Telefono:").grid(row=3, column=1)
        ttk.Label(self.ventana, text="300 1234567").grid(row=3, column=2)
        ttk.Label(self.ventana, text="Angel Camilo Gutierrez").grid(row=4, column=0)
        ttk.Label(self.ventana, text="Telefono:").grid(row=4, column=1)
        ttk.Label(self.ventana, text="300 1234567").grid(row=4, column=2)
        ttk.Label(self.ventana, text="Wilson Misal").grid(row=5, column=0)
        ttk.Label(self.ventana, text="Telefono:").grid(row=5, column=1)
        ttk.Label(self.ventana, text="300 1234567").grid(row=5, column=2)

        


#Clase Ventana Reporte
class VentanaReporte:
    def __init__(self, root):
        self.ventana = Toplevel(root)
        self.ventana.title("Reporte")
        self.ventana.geometry("600x400")
        
        # Etiqueta
        ttk.Label(self.ventana, text="Reporte:").grid(row=0, column=0, padx=10, pady=10)
        
        # Crear el Treeview para mostrar el reporte
        self.tree = ttk.Treeview(self.ventana, columns=("Nombre", "Cantidad", "Precio"), show="headings")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Precio", text="Precio")
        
        # Ajustar el tamaño de las columnas
        self.tree.column("Nombre", width=200, anchor="center")
        self.tree.column("Cantidad", width=100, anchor="center")
        self.tree.column("Precio", width=100, anchor="center")
        
        # Agregar datos al Treeview
        self.datos = [
            {"Nombre": "Producto A", "Cantidad": 10, "Precio": 15.5},
            {"Nombre": "Producto B", "Cantidad": 5, "Precio": 7.8},
            {"Nombre": "Producto C", "Cantidad": 8, "Precio": 12.0},
        ]
        for item in self.datos:
            self.tree.insert("", "end", values=(item["Nombre"], item["Cantidad"], item["Precio"]))
        
        # Colocar el Treeview en la ventana
        self.tree.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        
        # Agregar un botón para exportar a CSV
        ttk.Button(self.ventana, text="Exportar a CSV", command=self.exportar_csv).grid(row=2, column=0, pady=10)
        
    def exportar_csv(self):
        # Archivo CSV donde se exportarán los datos
        with open('reporte.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            # Escribir encabezado
            writer.writerow(["Nombre", "Cantidad", "Precio"])
            # Escribir los datos de los productos
            for item in self.datos:
                writer.writerow([item["Nombre"], item["Cantidad"], item["Precio"]])
        
        messagebox.showinfo("Exportación Exitosa", "El reporte ha sido exportado correctamente a reporte.csv")
    
#funcion de abrir registros
    def abrir_registro_cliente(self):
        VentanaCliente(self.root, self.agregar_cliente)

    def abrir_registro_repuesto(self):
        VentanaRepuesto(self.root, self.agregar_repuesto)

# Nueva funcionalidad: Generar archivo del inventario
    def generar_archivo_inventario(self):
        ruta_archivo = os.path.join(os.getcwd(), "inventario.txt")
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("INVENTARIO GENERAL\n")
            archivo.write("="*30 + "\n")
            
            # Exportar clientes
            archivo.write("Clientes Registrados:\n")
            if self.clientes:
                for cliente in self.clientes:
                    archivo.write(f"- {cliente.nombre} ({cliente.noDocumento})\n")
            else:
                archivo.write("No hay clientes registrados.\n")
            
            archivo.write("\n")

            # Exportar repuestos
            archivo.write("Repuestos Disponibles:\n")
            if self.repuestos:
                for repuesto in self.repuestos:
                    archivo.write(f"- {repuesto.id}: {repuesto.nombre} | Cantidad: {repuesto.cantidad} | Precio: {repuesto.precio}\n")
            else:
                archivo.write("No hay repuestos registrados.\n")
            
            archivo.write("\n")
            
            # Exportar órdenes
            archivo.write("Órdenes Registradas:\n")
            if self.ordenes:
                for orden in self.ordenes:
                    archivo.write(orden.mostrarOrden() + "\n")
            else:
                archivo.write("No hay órdenes registradas.\n")
                messagebox.showinfo("Éxito", f"Inventario exportado en: {ruta_archivo}")

if __name__ == "__main__":
    # Crear la ventana principal
    root = Tk()
    app = MenuPrincipal(root)
    root.mainloop()
