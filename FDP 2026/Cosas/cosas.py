

# Estructuras de control (if, else, elif, while, for)


# Operadores lógicos: <, <=, >, >=, ==, !=

# = singifica asignación ("es")
# == significa comparacion ("¿es?")

# IF
edad = int(input("Ingresa tu edad: "))

if edad < 20:
    print("tienes menos de 20 waw que joven")
elif edad == 20:
    print("tienes 20 wow")
elif edad > 20:
    print("tienes mas de 20 viejo")

# WHILE (Menu)

while True:
    opcion = int(input("Ingresa tu opcion"))

    print("1. Sacar dinero")
    print("2. Ver saldo")
    print("3. Salir")

    break

