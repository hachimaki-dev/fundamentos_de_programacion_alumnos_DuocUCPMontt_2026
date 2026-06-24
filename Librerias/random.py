from random import randint, choice
# 1. Un dado del 1 al 100
tirada = randint(1, 100)
print("Sacaste un:", tirada)
if tirada == 1:
    print("¡GANASTE EL PERSONAJE ULTRA-RARO!")
else:
    print("Sigue intentando...")
# 2. Elegir un enemigo al azar
enemigos = ["Orco", "Duende", "Dragón"]
rival = choice(enemigos)
print("¡Un", rival, "salvaje aparece!")