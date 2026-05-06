# Ejercicio 24: Generador de Nombres (Instagram)

print("=====================")
print("Generador de usuarios")
print("=====================")

usuarios = ["user_1", "user_2", "user_3", "user_4", "user_5"]

nombres = []

for usuario in usuarios:

    print(usuario)

    nombre = input("Ingrese un nombre para este usuario: ")

    nombres.append(nombre)

print("Lista de nombres:")

for nombre in nombres:
    print(nombre)