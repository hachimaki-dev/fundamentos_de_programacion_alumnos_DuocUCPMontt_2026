import random, sys

def forzar():
    if rol_escogido == 2:
        print("Abriste la puerta")
        return True
    else:
        print("No tienes las habilidades necesarias para forzar la puerta")
        return False
    
def ganzua():
    if rol_escogido == 1:
        print("Abriste la puerta")
        return True
    else:
        print("No tienes las habilidades necesarias para forzar la puerta")
        return False

def buscar_llave():
    if random.randint(1,2) == 1:
        print("Encontrase la llave, abriste la puerta")
        return True
    else:
        print("No encontraste la llave")
        return False

rol_escogido = 0

while True:
    print("1) Ladrón\n2) Guerrero")

    rol_escogido = int(input("\nIngresa tu opción: "))

    if rol_escogido == 1 or rol_escogido == 2:
        break

for i in range(3):
    flag = 0
    for x in range(3):
        print(f"Estas en la habitación {i + 1}")
        print(f"Intento N°{x + 1}")
        print("\n1) Forzar\n2) Ganzúa\n3) Buscar Llave")

        opcion_escogida = int(input("\nIngrese su opción: "))

        match opcion_escogida:
            case 1:
                if forzar():
                    break
                else:
                    flag += 1
                    continue
            case 2:
                if ganzua():
                    break
                else:
                    flag += 1
                    continue
            case 3:
                if buscar_llave():
                    break
                else:
                    flag += 1
                    continue
            case _:
                print("Opción invalida, perdiste un intento tontin")
        
    if flag == 3:
        print("----- Perdiste el juego -----")
        sys.exit()

print("\nGanaste!")