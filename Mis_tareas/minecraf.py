'''
Desarrolla un programa que simule una mesa de crafteo mediante un menú interactivo. El sistema debe solicitar continuamente una opción numérica al jugador entre las siguientes:
1. Craftear Espada de Diamante
2. Craftear Pico
3. Salir de la Mesa de Crafteo

Instrucciones:

Implementa un ciclo while True: que mantenga el menú constantemente activo, esperando la entrada del jugador.
Si el jugador selecciona la opción 1, el programa debe imprimir "¡Espada crafteada!". Si selecciona la opción 2, "¡Pico listo!".
Agrega una validación para controlar entradas inválidas: si ingresa un número distinto a 1, 2 o 3, imprime "Receta desconocida. Intenta nuevamente." y permite que el menú vuelva a solicitar una entrada válida en la siguiente iteración.
Utiliza la sentencia break para finalizar la ejecución del bucle única y estrictamente cuando el usuario seleccione la opción 3 ('Salir de la Mesa de Crafteo').
'''

opcion=0 
pregunta=0

print("Hora de craftear algo en tu mesa de crafteo amigo minecraftero")
while True:
    opcion=int(input("Que deseas crafreat 1: Espada 2: Pico 3: Salir "))
    if opcion==1:
        print("Espada crafteada")
    elif opcion == 2:
        print("Pico crafteado")
    elif opcion == 3:
        print("saliste de la mesa de crafteo...")
        break
    else:
        print("Por favor ingrese uno de los numeros en pantalla")
    
    pregunta=int(input("Desea seguir fabricando? 1=Si 2=No "))
    if pregunta == 1:
        print("A seguir crafteando")
    elif pregunta==2:
        print("Saliendo...")
        break
    else:
        print("ingrese un valor valido")
        continue

print("====Crafteo terminado====")