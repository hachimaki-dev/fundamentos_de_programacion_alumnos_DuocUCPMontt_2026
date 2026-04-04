número_secreto = 20
respuesta = -1 
intentos = 0
while intentos < 5:
    adivinanza = int(input("Adivina el número secreto (entre el 1 al 50"))
    intentos += 1 

if adivinanza < número_secreto:
    print("Demasiado ALTO, intentalo de nuevo!")

elif adivinanza > número_secreto:                          
   print("Demasiado BAJO, intentalo de nuevo!")

if respuesta != número_secreto and intentos == 5:
    print("Ganaste") 
    print ("iFelicidades crack! Has adivinado el número secreto en", intentos, "intentos!") 

