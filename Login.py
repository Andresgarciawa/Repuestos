from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Datos de login quemados en el código
login_usuario = "usuario123"
login_contraseña = "contraseñaSegura"

# Función para verificar el inicio de sesión
def verificar_login():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    
    if usuario == login_usuario and contraseña == login_contraseña:
        messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Crear la ventana principal
ventana = Tk()

# Configuración de la ventana
ventana.title("Inicio de Sesión")
ventana.geometry("300x200")

# Etiqueta y entrada para el usuario
label_usuario = Label(ventana, text="Usuario:")
label_usuario.pack(pady=5)
entry_usuario = Entry(ventana)
entry_usuario.pack(pady=5)

# Etiqueta y entrada para la contraseña
label_contraseña = Label(ventana, text="Contraseña:")
label_contraseña.pack(pady=5)
entry_contraseña = Entry(ventana, show="*")
entry_contraseña.pack(pady=5)

# Botón para iniciar sesión
boton_login = Button(ventana, text="Iniciar Sesión", command=verificar_login)
boton_login.pack(pady=10)

# Etiqueta de versión con un estilo más discreto
ttk.Label(
    ventana, 
    text="v1.0.0 | © 2024",
    font=('Helvetica', 8),
    foreground='gray'
).pack(pady=10)  # Cambié grid a pack para mantener la consistencia

# Ejecutar la ventana
ventana.mainloop()