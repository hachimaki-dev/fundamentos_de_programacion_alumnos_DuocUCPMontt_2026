#simulacion de mesa de crafteo

print("Bienvenido a la mesa de crafteo")

while True:
    print("Que desea fabricar")
    print("1. Craftear Espada de Diamante")
    print("2. Craftear Pico")
    print("3. Salir de la Mesa de Crafteo")

    opcion = int(input("seleciona una opcion: "))
    
    if opcion == 1:
        print("espada crafteada")
    elif opcion == 2: 
        print("pico crafteado")
    elif opcion == 3: 
        print("saliendo de la mesa de crafteo")
        break 
    else:
        print("receta desconocida, intenta nuevamente")
    

