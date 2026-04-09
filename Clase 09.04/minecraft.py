""" 
Reto 1: Minecraft - Menú de Crafteo
Crea un programa que ofrezca un menú infinito con 3 opciones:
1. Craftear Espada de Diamante
2. Craftear Pico
3. Salir de la Mesa de Crafteo

Instrucciones:

Usa un while True: y rompe el ciclo con break SOLO si el usuario elige la opción 3.
Si elige 1, imprime "¡Espada crafteada!". Si elige 2, imprime "¡Pico listo!".
Si elige una opción inválida (ej. 4), imprime "Receta desconocida" y el menú debe volver a mostrarse.
"""
while True:
    print("""1. Craftear Espada de Diamante
2. Craftear Pico
3. Salir de la Mesa de Crafteo""")
    respuesta = int(input())
    if respuesta == 1:
        print("¡Espada crafteada!")
    elif respuesta == 2:
        print("¡Pico listo!")
    elif respuesta == 3:
        break
    else:
        print("Receta desconocida")