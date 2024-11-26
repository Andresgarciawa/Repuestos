from tkinter import *
from tkinter import messagebox
from tkinter import ttk, messagebox

# Datos de login quemados en el código
login_usuario = "usuario123"
login_contraseña = "contraseñaSegura"

    # Etiqueta de versión con un estilo más discreto
    ttk.Label(
        main_frame, 
        text="v1.0.0 | © 2024",
        font=('Helvetica', 8),
        # Color gris
        foreground='gray'  
        ).grid(row=4, column=0, columnspan=2, pady=10)
    

# Función para verificar el inicio de sesión
def verificar_login():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    
    if usuario == login_usuario and contraseña == login_contraseña:
        messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Crear la ventana principal
ventana = tk.Tk()

# Configuración de la ventana
ventana.title("Inicio de Sesión")
ventana.geometry("300x200")

# Etiqueta y entrada para el usuario
label_usuario = tk.Label(ventana, text="Usuario:")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(ventana)
entry_usuario.pack(pady=5)

# Etiqueta y entrada para la contraseña
label_contraseña = tk.Label(ventana, text="Contraseña:")
label_contraseña.pack(pady=5)
entry_contraseña = tk.Entry(ventana, show="*")
entry_contraseña.pack(pady=5)

# Botón para iniciar sesión
boton_login = tk.Button(ventana, text="Iniciar Sesión", command=verificar_login)
boton_login.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()

def main():
    root = Tk()
    app = MenuPrincipal(root)
    root.mainloop()