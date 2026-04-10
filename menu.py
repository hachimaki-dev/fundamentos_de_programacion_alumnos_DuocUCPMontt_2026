#Desarrolla un programa que simule una mesa de crafteo mediante un menú interactivo. El sistema debe solicitar continuamente una opción numérica al jugador entre las siguientes:
#1. Craftear Espada de Diamante
#2. Craftear Pico
#3. Salir de la Mesa de Crafteo

#Instrucciones:

#Implementa un ciclo while True: que mantenga el menú constantemente activo, esperando la entrada del jugador.
#Si el jugador selecciona la opción 1, el programa debe imprimir "¡Espada crafteada!". Si selecciona la opción 2, "¡Pico listo!".
#Agrega una validación para controlar entradas inválidas: si ingresa un número distinto a 1, 2 o 3, imprime "Receta desconocida. Intenta nuevamente." y permite que el menú vuelva a solicitar una entrada válida en la siguiente iteración.
#Utiliza la sentencia break para finalizar la ejecución del bucle única y estrictamente cuando el usuario seleccione la opción 3 ('Salir de la Mesa de Crafteo').
crafteo_espada = 1
crafteo = 2
salir = 3
while True:
    print("Bienvenido al crafteo")
    print("1. espada de diamante\n 2. pico de madera \n 3.salir de la mesa de crafteo")
    numero = int(input("ingrese numero"))
  
    if numero == crafteo_espada:
        print("espada crafteada :)")

    elif numero == crafteo:
        print("pico crafteado")
  
    elif numero == salir:
        print("saliste de la mesa de crafteo")
        break
    else:
        prin
        
