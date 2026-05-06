contador = 0
while True:
    clave = input("ingrese la clave ")
    contador +=1
    if contador == 3:
        print("Bloqueo de tarjeta")
        break
