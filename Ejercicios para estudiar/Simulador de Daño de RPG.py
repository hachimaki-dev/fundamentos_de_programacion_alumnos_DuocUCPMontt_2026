#El jefe final tiene 1000 puntos de vida iniciales.
#Usa un ciclo while que se repita mientras la vida del jefe sea mayor que 0.
#Dentro del ciclo, pide al usuario ingresar el daño del ataque (entero).
#Si el daño es menor a 0, muestra un mensaje "El ataque falló" y no restes vida.
#Si el daño es mayor o igual a 0, réstalo de la vida del jefe y muestra la vida restante.
#Si la vida es 0 o menos, rompe el ciclo o deja que termine naturalmente, y muestra "¡Jefe derrotado!".

Jefe_final=1000
while Jefe_final > 0:
    Ataque = int(input("Ingrese ataque: "))
    if Ataque < 0:
        print("¡El ataque falló!")
    else:
        Jefe_final = Jefe_final - Ataque
        print ("Vida restante:",Jefe_final)
print("¡Jefe derrotado!")