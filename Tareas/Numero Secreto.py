numero_secreto = 42
bandera = True
contador = 0

print("Bienvenido a este videojuego de Python, yo estare pensando en un numero y tu lo tendras que adivinar")
print("EMPEZEMOSSSSS!!!!!")


while bandera:
    contador = contador + 1
    numero_ingresado = int(input("Por favor, ingrese el numero que creas que pienso"))
    if contador == 1 and numero_ingresado == numero_secreto:
        print("FELICIDADES, DE SEGURO ERES PYTHONSIQUICO, ADIVINASTE A LA PRIMERAAA")
        import sys
        sys.exit ()
    elif numero_ingresado < numero_secreto:
        print("Una lastima, el numero secreto es más alto")
    elif numero_ingresado > numero_secreto:
        print("Una lastima, el numero secreto es más bajo")
    else:
        print("Por favor ingresa un NúMERO VáLIDO")
    if numero_ingresado == numero_secreto:
        print("Felicidades, haz acertado al número secreto")
        print(f"Solo te tomo la cantidad de {contador} intentos")
        bandera = False
        break
