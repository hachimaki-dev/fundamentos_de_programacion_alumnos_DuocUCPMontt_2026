num1 = int(input("Minimo del rango: "))
num2 = int(input("Maximo del rango: "))
intentos = 0
from random import randint
numero = randint(num1, num2)
if (numero % 2) != 0:
    if numero +1 < num2:
        numero = numero +1
    else:
        numero = numero -1
while intentos != 3:
    numero_jugador = int(input("Intente adivinar: "))
    intentos = intentos +1
    if numero_jugador != numero:
        if intentos == 1:
            primer_numero = numero_jugador
            if numero_jugador < numero:
                print(f"Su numero es mayor que {numero_jugador}")
            else:
                print(f"Su numero es menor que {numero_jugador}")
        elif intentos == 2:
            segundo_numero = numero_jugador

            if numero_jugador < numero:
                if (numero - primer_numero) < (numero - segundo_numero):
                    print(f"Su numero es mayor que {numero_jugador}")
                    print(f"El numero se acerca mas al {primer_numero} que al {segundo_numero}")
                else:
                    print(f"Su numero es mayor que {numero_jugador}")
                    print(f"El numero se acerca mas al {segundo_numero} que al {primer_numero}")
            else:
                if (numero - primer_numero) > (numero - segundo_numero):
                        print(f"Su numero es menor que {numero_jugador}")
                        print(f"El numero se acerca mas al {primer_numero} que al {segundo_numero}")
                else:
                        print(f"Su numero es menor que {numero_jugador}")
                        print(f"El numero se acerca mas al {segundo_numero} que al {primer_numero}")
        elif intentos ==3:
            print(f"Perdiste, el numero era {numero}")
    else:
        print(f"Felicidades, usted gana en su {intentos} intento")
        break