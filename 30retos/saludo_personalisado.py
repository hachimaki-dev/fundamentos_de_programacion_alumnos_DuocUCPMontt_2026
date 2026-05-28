
def saludo_personalizado(nombre):
    nombre_del_usuario = nombre
    return f"¡Hola {nombre_del_usuario}, bienvenido al sistema!" f"(Quedas registrado como {nombre})"

print(saludo_personalizado(input("Ingresa tu nombre de usuario: ")))
    