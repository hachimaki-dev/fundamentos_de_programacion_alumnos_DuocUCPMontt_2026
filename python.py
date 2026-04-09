import time
opcion_escogida = 0
print ("--MESA DE CRAFTEO")
print("1. Craftear Espada de diamante")
print ("2 . Craftear pico")
print("3 . Salir de la mesa de crafteo")
while True:
    opcion_escogida = int(input("Escoga una de las 3 opciones"))
    if opcion_escogida == 1 :
        print("Cargando espada..")
        time.sleep(5)
        print("Espada crafteada!")
    elif opcion_escogida == 2 :
        print("Cargando pico..")
        time.sleep(5)
        print("Pico creado!")
    elif opcion_escogida == 3:
        print("Ha salido del menu de crafteo")
    else :
        print("RECETA DESCONOCIDA")