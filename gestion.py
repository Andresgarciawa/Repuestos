from tkinter import *
from tkinter import ttk, messagebox, Toplevel, StringVar, Listbox, Text, END, N, W, E, S
from cliente import Cliente
from repuesto import Repuesto
from orden import Orden
from vendedor import Vendedor
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
            command=self.abrir_registro_vendedor,  # Usa este método
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

    # Método para abrir registro de vendedor
    def abrir_registro_vendedor(self):
        VentanaVendedor(self.root, self.vendedor)
    
    def agregar_vendedor(self, vendedor):
        self.vendedor.append(vendedor)
    
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
        self.ventana.title("Gestión de Clientes")
        self.ventana.geometry("600x400")

        # Frame superior para los campos de entrada
        frame_campos = ttk.Frame(self.ventana, padding="10")
        frame_campos.pack(side=TOP, fill=X)
        
        ttk.Label(frame_campos, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.nombre_var = StringVar()
        ttk.Entry(frame_campos, textvariable=self.nombre_var).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_campos, text="No. Documento:").grid(row=0, column=2, padx=5, pady=5)
        self.no_documento_var = StringVar()
        ttk.Entry(frame_campos, textvariable=self.no_documento_var).grid(row=0, column=3, padx=5, pady=5)
        
        # Botones para acciones
        ttk.Button(frame_campos, text="Registrar", command=self.guardar_cliente).grid(row=1, column=0, padx=5, pady=10)
        ttk.Button(frame_campos, text="Editar", command=self.editar_cliente).grid(row=1, column=1, padx=5, pady=10)
        ttk.Button(frame_campos, text="Eliminar", command=self.eliminar_cliente).grid(row=1, column=2, padx=5, pady=10)
        ttk.Button(frame_campos, text="Limpiar", command=self.limpiar_campos).grid(row=1, column=3, padx=5, pady=10)
        
        # Tabla para visualizar los clientes
        self.tabla = ttk.Treeview(self.ventana, columns=("Nombre", "No. Documento"), show="headings")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("No. Documento", text="No. Documento")
        self.tabla.pack(fill=BOTH, expand=True)

        # Evento de selección en la tabla
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_cliente)

        # Variable para el cliente seleccionado
        self.cliente_seleccionado = None

        # Cargar los clientes iniciales en la tabla
        self.actualizar_tabla()

    def guardar_cliente(self):
        try:
            nombre = self.nombre_var.get()
            no_documento = self.no_documento_var.get()

            # Validar campos
            if not nombre or not no_documento:
                raise ValueError("El nombre y el número de documento son obligatorios")

            # Verificar que el número de documento no esté duplicado
            if any(cliente.no_documento == no_documento for cliente in self.datoC):
                raise ValueError("El número de documento ya existe")

            # Crear y agregar el nuevo cliente
            nuevo_cliente = Cliente(nombre, no_documento)
            self.datoC.append(nuevo_cliente)

            # Actualizar la tabla y limpiar los campos
            self.actualizar_tabla()
            self.limpiar_campos()
            messagebox.showinfo("Éxito", "Cliente registrado exitosamente")
        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")

    def editar_cliente(self):
        if not self.cliente_seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un cliente para editar")
            return

        try:
            nombre = self.nombre_var.get()
            no_documento = self.no_documento_var.get()

            # Validar campos
            if not nombre or not no_documento:
                raise ValueError("El nombre y el número de documento son obligatorios")

            # Verificar que el número de documento no se duplique al editar
            if any(cliente.no_documento == no_documento and cliente != self.cliente_seleccionado for cliente in self.datoC):
                raise ValueError("El número de documento ya existe")

            # Actualizar los datos del cliente seleccionado
            self.cliente_seleccionado.nombre = nombre
            self.cliente_seleccionado.no_documento = no_documento

            # Actualizar la tabla y limpiar los campos
            self.actualizar_tabla()
            self.limpiar_campos()
            messagebox.showinfo("Éxito", "Cliente editado exitosamente")
        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")

    def eliminar_cliente(self):
        if not self.cliente_seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un cliente para eliminar")
            return

        # Confirmar eliminación
        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este cliente?"):
            self.datoC.remove(self.cliente_seleccionado)
            self.actualizar_tabla()
            self.limpiar_campos()
            messagebox.showinfo("Éxito", "Cliente eliminado exitosamente")

    def actualizar_tabla(self):
        # Limpiar la tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Agregar los clientes a la tabla
        for cliente in self.datoC:
            self.tabla.insert("", END, values=(cliente.nombre, cliente.no_documento))

    def seleccionar_cliente(self, event):
        try:
            item = self.tabla.selection()[0]
            values = self.tabla.item(item, "values")
            self.cliente_seleccionado = next(c for c in self.datoC if c.no_documento == values[1])

            # Llenar los campos con los valores seleccionados
            self.nombre_var.set(self.cliente_seleccionado.nombre)
            self.no_documento_var.set(self.cliente_seleccionado.no_documento)
        except Exception:
            self.cliente_seleccionado = None

    def limpiar_campos(self):
        self.nombre_var.set("")
        self.no_documento_var.set("")


class VentanaRepuesto:
    def __init__(self, root, datoR):
        self.datoRepuesto = datoR  # Recibe la lista de repuestos
        self.ventana = Toplevel(root)
        self.ventana.title("Gestión de Repuestos")
        self.ventana.geometry("600x400")
        
        # Frame superior para los campos de entrada
        frame_campos = ttk.Frame(self.ventana, padding="10")
        frame_campos.pack(side=TOP, fill=X)
        
        ttk.Label(frame_campos, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        self.id_var = StringVar()
        ttk.Entry(frame_campos, textvariable=self.id_var).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_campos, text="Nombre:").grid(row=0, column=2, padx=5, pady=5)
        self.nombre_var = StringVar()
        ttk.Entry(frame_campos, textvariable=self.nombre_var).grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame_campos, text="Precio:").grid(row=1, column=0, padx=5, pady=5)
        self.precio_var = StringVar()
        ttk.Entry(frame_campos, textvariable=self.precio_var).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_campos, text="Cantidad:").grid(row=1, column=2, padx=5, pady=5)
        self.cantidad_var = StringVar()
        ttk.Entry(frame_campos, textvariable=self.cantidad_var).grid(row=1, column=3, padx=5, pady=5)

        # Botones para acciones
        ttk.Button(frame_campos, text="Registrar", command=self.guardar_repuesto).grid(row=2, column=0, padx=5, pady=10)
        ttk.Button(frame_campos, text="Editar", command=self.editar_repuesto).grid(row=2, column=1, padx=5, pady=10)
        ttk.Button(frame_campos, text="Eliminar", command=self.eliminar_repuesto).grid(row=2, column=2, padx=5, pady=10)
        ttk.Button(frame_campos, text="Limpiar", command=self.limpiar_campos).grid(row=2, column=3, padx=5, pady=10)

        # Tabla para visualizar los repuestos
        self.tabla = ttk.Treeview(self.ventana, columns=("ID", "Nombre", "Precio", "Cantidad"), show="headings")
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Precio", text="Precio")
        self.tabla.heading("Cantidad", text="Cantidad")
        self.tabla.pack(fill=BOTH, expand=True)

        # Evento de selección en la tabla
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_repuesto)

        # Variable para el repuesto seleccionado
        self.repuesto_seleccionado = None

        # Cargar los repuestos iniciales en la tabla
        self.actualizar_tabla()

    def guardar_repuesto(self):
        try:
            id_repuesto = self.id_var.get()
            nombre = self.nombre_var.get()
            precio = float(self.precio_var.get())
            cantidad = int(self.cantidad_var.get())

            # Validar campos
            if not id_repuesto or not nombre:
                raise ValueError("ID y Nombre son obligatorios")

            # Verificar que el ID no esté duplicado
            if any(r.id == id_repuesto for r in self.datoRepuesto):
                raise ValueError("El ID del repuesto ya existe")

            # Crear y agregar el nuevo repuesto
            nuevo_repuesto = Repuesto(id_repuesto, nombre, precio, cantidad)
            self.datoRepuesto.append(nuevo_repuesto)

            # Actualizar la tabla y limpiar los campos
            self.actualizar_tabla()
            self.limpiar_campos()
            messagebox.showinfo("Éxito", "Repuesto registrado exitosamente")
        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")

    def editar_repuesto(self):
        if not self.repuesto_seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un repuesto para editar")
            return

        try:
            id_repuesto = self.id_var.get()
            nombre = self.nombre_var.get()
            precio = float(self.precio_var.get())
            cantidad = int(self.cantidad_var.get())

            # Actualizar los datos del repuesto seleccionado
            self.repuesto_seleccionado.id = id_repuesto
            self.repuesto_seleccionado.nombre = nombre
            self.repuesto_seleccionado.precio = precio
            self.repuesto_seleccionado.cantidad = cantidad

            # Actualizar la tabla y limpiar los campos
            self.actualizar_tabla()
            self.limpiar_campos()
            messagebox.showinfo("Éxito", "Repuesto editado exitosamente")
        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")

    def eliminar_repuesto(self):
        if not self.repuesto_seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un repuesto para eliminar")
            return

        # Confirmar eliminación
        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este repuesto?"):
            self.datoRepuesto.remove(self.repuesto_seleccionado)
            self.actualizar_tabla()
            self.limpiar_campos()
            messagebox.showinfo("Éxito", "Repuesto eliminado exitosamente")

    def actualizar_tabla(self):
        # Limpiar la tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Agregar los repuestos a la tabla
        for repuesto in self.datoRepuesto:
            self.tabla.insert("", END, values=(repuesto.id, repuesto.nombre, repuesto.precio, repuesto.cantidad))

    def seleccionar_repuesto(self, event):
        try:
            item = self.tabla.selection()[0]
            values = self.tabla.item(item, "values")
            self.repuesto_seleccionado = next(r for r in self.datoRepuesto if r.id == values[0])

            # Llenar los campos con los valores seleccionados
            self.id_var.set(self.repuesto_seleccionado.id)
            self.nombre_var.set(self.repuesto_seleccionado.nombre)
            self.precio_var.set(self.repuesto_seleccionado.precio)
            self.cantidad_var.set(self.repuesto_seleccionado.cantidad)
        except Exception:
            self.repuesto_seleccionado = None

    def limpiar_campos(self):
        self.id_var.set("")
        self.nombre_var.set("")
        self.precio_var.set("")
        self.cantidad_var.set("")

from tkinter import *
from tkinter import ttk, messagebox

class VentanaVendedor:
    def __init__(self, root, vendedores):
        # Se crea la ventana emergente
        self.ventana = Toplevel(root)
        self.ventana.title("Gestión de Vendedores")
        self.ventana.geometry("600x400")
        
        # Almacenar la lista de vendedores
        self.vendedores = vendedores
        
        # Frame superior para los campos de entrada
        frame_campos = ttk.Frame(self.ventana, padding="10")
        frame_campos.pack(side=TOP, fill=X)
        
        # Campos para registrar al vendedor
        ttk.Label(frame_campos, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.nombre_var = StringVar()
        ttk.Entry(frame_campos, textvariable=self.nombre_var).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_campos, text="ID:").grid(row=0, column=2, padx=5, pady=5)
        self.id_var = StringVar()
        ttk.Entry(frame_campos, textvariable=self.id_var).grid(row=0, column=3, padx=5, pady=5)
        
        # Botones de acción
        ttk.Button(frame_campos, text="Registrar", command=self.registrar_vendedor).grid(row=1, column=0, padx=5, pady=10)
        ttk.Button(frame_campos, text="Editar", command=self.editar_vendedor).grid(row=1, column=1, padx=5, pady=10)
        ttk.Button(frame_campos, text="Eliminar", command=self.eliminar_vendedor).grid(row=1, column=2, padx=5, pady=10)
        ttk.Button(frame_campos, text="Limpiar", command=self.limpiar_campos).grid(row=1, column=3, padx=5, pady=10)
        
        # Tabla para visualizar los vendedores
        self.tabla = ttk.Treeview(self.ventana, columns=("Nombre", "ID"), show="headings")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("ID", text="ID")
        self.tabla.pack(fill=BOTH, expand=True)

        # Evento para seleccionar un vendedor en la tabla
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_vendedor)

        # Variable para almacenar el vendedor seleccionado
        self.vendedor_seleccionado = None

        # Cargar los vendedores en la tabla
        self.actualizar_tabla()

    def registrar_vendedor(self):
        try:
            nombre = self.nombre_var.get().strip()
            id_vendedor = self.id_var.get().strip()

            # Validar campos
            if not nombre or not id_vendedor:
                raise ValueError("Debe completar todos los campos")

            # Verificar si el ID ya existe
            if any(v['id'] == id_vendedor for v in self.vendedores):
                raise ValueError("El ID de vendedor ya existe")

            # Crear y agregar el nuevo vendedor
            nuevo_vendedor = {'nombre': nombre, 'id': id_vendedor}
            self.vendedores.append(nuevo_vendedor)

            # Actualizar la tabla y limpiar los campos
            self.actualizar_tabla()
            self.limpiar_campos()
            messagebox.showinfo("Éxito", "Vendedor registrado exitosamente")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def editar_vendedor(self):
        if not self.vendedor_seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un vendedor para editar")
            return

        try:
            nombre = self.nombre_var.get().strip()
            id_vendedor = self.id_var.get().strip()

            # Validar campos
            if not nombre or not id_vendedor:
                raise ValueError("Debe completar todos los campos")

            # Verificar que el ID no se duplique al editar
            if any(v['id'] == id_vendedor and v != self.vendedor_seleccionado for v in self.vendedores):
                raise ValueError("El ID de vendedor ya existe")

            # Actualizar los datos del vendedor seleccionado
            self.vendedor_seleccionado['nombre'] = nombre
            self.vendedor_seleccionado['id'] = id_vendedor

            # Actualizar la tabla y limpiar los campos
            self.actualizar_tabla()
            self.limpiar_campos()
            messagebox.showinfo("Éxito", "Vendedor editado exitosamente")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def eliminar_vendedor(self):
        if not self.vendedor_seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un vendedor para eliminar")
            return

        # Confirmar eliminación
        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este vendedor?"):
            self.vendedores.remove(self.vendedor_seleccionado)
            self.actualizar_tabla()
            self.limpiar_campos()
            messagebox.showinfo("Éxito", "Vendedor eliminado exitosamente")

    def actualizar_tabla(self):
        # Limpiar la tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Agregar los vendedores a la tabla
        for vendedor in self.vendedores:
            self.tabla.insert("", END, values=(vendedor['nombre'], vendedor['id']))

    def seleccionar_vendedor(self, event):
        try:
            item = self.tabla.selection()[0]
            values = self.tabla.item(item, "values")
            self.vendedor_seleccionado = next(v for v in self.vendedores if v['id'] == values[1])

            # Llenar los campos con los valores seleccionados
            self.nombre_var.set(self.vendedor_seleccionado['nombre'])
            self.id_var.set(self.vendedor_seleccionado['id'])
        except Exception:
            self.vendedor_seleccionado = None

    def limpiar_campos(self):
        self.nombre_var.set("")
        self.id_var.set("")
        self.vendedor_seleccionado = None

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
    
    def abrir_registro_vendedor(self):
        VentanaVendedor(self.root, self.abrir_registro_vendedor)

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
