bandera = True
arma = 0
print("Bienvenido a la Armeria de Valorant")

while bandera:
    print("Tenemos 5 armas")
    print("1. Arma 1")
    print("2. Arma 2")
    print("3. Arma 3")
    print("4. Arma 4")
    print("5. Arma 5")
    arma_escogida = int(input("Seleccione el arma que desea comprar"))
    if arma_escogida <= 3 or arma_escogida == 5:
        arma = arma_escogida 
        print(f"Haz comprado la arma {arma} con exito")
        break
    elif arma_escogida == 4:
        print("Arma agotada")
        print("Seleccione otra opción")
        continue
    else:
        print("Seleccione una opcion valida")