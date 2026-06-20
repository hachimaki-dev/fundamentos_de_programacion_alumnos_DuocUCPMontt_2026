""" Desarrolla un programa que simule una mesa de crafteo mediante un menú 
interactivo. El sistema debe solicitar continuamente una opción numérica 
al jugador entre las siguientes:

1. Craftear Espada de Diamante
2. Craftear Pico
3. Salir de la Mesa de Crafteo

Instrucciones:

Implementa un ciclo while True: que mantenga el menú constantemente 
activo, esperando la entrada del jugador.

Si el jugador selecciona la opción 1, el programa debe imprimir 
"¡Espada crafteada!". Si selecciona la opción 2, "¡Pico listo!".

Agrega una validación para controlar entradas inválidas: si ingresa un número
 distinto a 1, 2 o 3, imprime "Receta desconocida. Intenta nuevamente." y 
 permite que el menú vuelva a solicitar una entrada válida en la siguiente 
 iteración.

Utiliza la sentencia break para finalizar la ejecución del bucle única y 
estrictamente cuando el usuario seleccione la opción 3 
('Salir de la Mesa de Crafteo')."""

menu = 0

while menu == 0:
    menu = int(input("1. craftear una espada de diamante. 2.craftear pico 3.salir de la mesa de crafteo"))
    
    if menu == 1:
        print(" espada crafteada")

    elif menu ==2:
        print("pico listo")

    elif menu ==3:
        print("saliendo de la mesa")

    else:
        print("receta desconocida intenta nuevamente") 
