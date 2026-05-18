from random import randint

print("ADIVINA EL NUMERO DEL 1 AL 10:")

minimo = int(input())
maximo = int(input())

numero = randint(minimo , maximo)

if numero % 2 != 0:
    if numero + 1 <= maximo:
        numero = numero + 1
    else:
        numero = numero - 1
        
for intento in range (1, 4):
    intento_jugador = int(input())
    
    if intento_jugador == numero:
        print("Felicitaciones, pudiste adivinar")
        break
    else:
        if intento == 1:
            if intento_jugador > numero:
                print("El numero es menor")
            else:
                print("El numero es mayor")
             
             
        elif intento == 2:
            if intento_jugador > numero:
                print("El numero es menor")
            else:
                print("EL numero es mayor")
            if abs(intento_jugador - numero) <= 3:
                print("estas cerca")
            else:
                print("Estas lejos")
                
        elif intento == 3 :
            print("El numero era",numero)
        
             
          