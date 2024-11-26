# Definimos una variable para el login
login_usuario = "usuario123"  # Aquí puedes poner el nombre de usuario deseado
login_contraseña = "contraseñaSegura"  # Aquí puedes poner la contraseña deseada

# Función para simular un inicio de sesión
def iniciar_sesion(usuario, contraseña):
    if usuario == login_usuario and contraseña == login_contraseña:
        return "Inicio de sesión exitoso"
    else:
        return "Usuario o contraseña incorrectos"

# Ejemplo de uso
resultado = iniciar_sesion("usuario123", "contraseñaSegura")
print(resultado)  # Esto imprimirá "Inicio de sesión exitoso"