print ("=======================")
print ("===Adivina el número===")
print ("=======================\n")


import random

print ("Bienvenido al juego de adivinanza en python")
print ("Estoy pensando en un número entre 1 al 100")
print ("¿Créss adivinar cual es?\n")

numero_secreto = random.randint(1, 100)
intentos = 0
adivinado = False

while not adivinado:
    try:
        adivinanza = int(input ("Ingrese su número : "))
        intentos += 1 

        if adivinanza < numero_secreto :
            print ("Número demasiado bajo, Vuelva a intentarlo")
        elif adivinanza > numero_secreto :
            print ("Número demasiado alto, Vuelva a intentarlo") 
        
        else: 
            adivinado = True
            print (f"Has adivinado el número, el número era {numero_secreto} en {intentos}.")

    except ValueError:
        print ("Por favor, ingrese un número valido")
