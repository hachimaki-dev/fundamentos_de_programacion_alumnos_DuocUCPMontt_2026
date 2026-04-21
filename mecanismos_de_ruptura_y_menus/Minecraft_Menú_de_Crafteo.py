"""
Desarrolla un programa que simule una mesa de crafteo mediante un menú interactivo. El sistema debe solicitar continuamente una opción numérica al jugador entre las siguientes:
1. Craftear Espada de Diamante
2. Craftear Pico
3. Salir de la Mesa de Crafteo 
"""

"""
Implementa un ciclo while True: que mantenga el menú constantemente activo, esperando la entrada del jugador.
Si el jugador selecciona la opción 1, el programa debe imprimir "¡Espada crafteada!". Si selecciona la opción 2, "¡Pico listo!".
Agrega una validación para controlar entradas inválidas: si ingresa un número distinto a 1, 2 o 3, imprime "Receta desconocida. Intenta nuevamente." y permite que el menú vuelva a solicitar una entrada válida en la siguiente iteración.
Utiliza la sentencia break para finalizar la ejecución del bucle única y estrictamente cuando el usuario seleccione la opción 3 ('Salir de la Mesa de Crafteo').
"""

ciclo_de_crafteo = True

while ciclo_de_crafteo == True:
    print("- Menu de crafteo -")
    print("1. Craftear Espada de Diamante")
    print("2. Craftear Pico") # Hehehe, pico XD
    print("3. Salir de la Mesa de Crafteo")
    try:
        seleccion = int(input("[]: "))
        if seleccion == 1:
            print("\n - - - - - - - - - - - - - - - - -")
            print("Espada Crafteada!")
            print("- - - - - - - - - - - - - - - - - \n")
            continue
        if seleccion == 2:
            print("\n - - - - - - - - - - - - - - - - -")
            print("Pico listo!")
            print("- - - - - - - - - - - - - - - - - \n")
            continue
        if seleccion ==3:
            print("\n - - - - - - - - - - - - - - - - -")
            print("Terminando menu de crafteo ^w^")
            print("- - - - - - - - - - - - - - - - - \n")
            break
        else:
            print("Receta invalida!")
    except:
        print("Receta invalida!")