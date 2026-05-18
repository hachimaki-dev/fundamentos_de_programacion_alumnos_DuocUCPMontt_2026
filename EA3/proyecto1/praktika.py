from random import randint
ran1 = int(input("Ingrese limite inferior: "))
ran2 = int(input("ingrese limite superior: "))
numerorand = randint(ran1, ran2)
intentos = 3
adivinanza = 0
adivinanza2 = 0
adivinanza3 = 0
def espar(numerorand, ran1, ran2):
    if numerorand % 2 != 0 and numerorand + 1 in range(ran1, ran2):
        numerorand += 1
    elif numerorand % 2 != 0 and numerorand + 1 not in range(ran1, ran2):
        numerorand -= 1
espar(numerorand,ran1, ran2)
while intentos > 0:
    if intentos == 3:
        adivinanza = int(input("intente adivinar: "))
    elif intentos == 2:
        adivinanza2 = int(input("intente adivinar: "))
    if adivinanza == numerorand and intentos == 3:
        print("Felicitaciones, adivino en el primer intento")
        break
    if adivinanza2 == numerorand and intentos == 2:
        print("Felicitaciones adivino en su segundo intento")
        break
    if intentos <= 3:
        if numerorand > adivinanza:
            print("El numero es mayor.")
        elif numerorand < adivinanza:
            print("el numero es menor")
    if intentos == 2:
        diferencia1 = abs(numerorand - adivinanza)
        diferencia2 = abs(numerorand - adivinanza2)
        print("Te dare una pista:")
        if diferencia1 > diferencia2:
            print(f"el numero que buscas esta mas cerca de {adivinanza2} que de {adivinanza}")
        elif diferencia1 < diferencia2:
            print(f"el numero que buscas esta mas cerca de {adivinanza} que de {adivinanza2}")
    if intentos == 1:
        adivinanza3 = int(input("intente una ultima vez: "))
        if adivinanza3 != numerorand:
            print("Perdiste.")
            print(f"el numero era: {numerorand}")
        else:
            print("Felicidades adivinaste el numero")
    intentos -= 1