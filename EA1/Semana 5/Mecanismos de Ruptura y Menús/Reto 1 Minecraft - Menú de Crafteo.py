# 💎 Reto 1: Minecraft - Menú de Crafteo
# Crea un programa que ofrezca un menú infinito con 3 opciones:
# 1. Craftear Espada de Diamante
# 2. Craftear Pico
# 3. Salir de la Mesa de Crafteo

# Instrucciones:

# Usa un while True: y rompe el ciclo con break SOLO si el usuario elige la opción 3.
# Si elige 1, imprime "¡Espada crafteada!". Si elige 2, imprime "¡Pico listo!".
# Si elige una opción inválida (ej. 4), imprime "Receta desconocida" y el menú debe volver a mostrarse.

while True:
    opcion = int(input("1. Crafter Espada de diamante\n" \
    "2. Crafter Pico\n" \
    "3. Salir de la Mesa de Crafteo\n" \
    "Eliga una opción: "))

    if opcion == 3:
        break

    if opcion == 1:
        print(" ")
        print("¡Espada crafteada!")
        print(" ")
    elif opcion == 2:
        print(" ")
        print("¡Pico listo!")
        print(" ")
    else:
        print(" ")
        print("Receta desconocida")
        print(" ")