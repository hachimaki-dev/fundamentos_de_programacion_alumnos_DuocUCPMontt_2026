"""
🎤 Reto 2: Bias K-Pop Validator
Crea un programa que te pregunte a qué grupo quieres unirte. Solo te dejará pasar si ingresas nombres de grupos válidos.

Instrucciones:

El usuario debe ingresar el nombre de su grupo favorito.
Mientras el grupo no sea "BTS" y no sea "BLACKPINK" y no sea "Stray Kids", el programa seguirá pidiendo un grupo válido. (Ojo: usa combinación de and u or con !=).
Cuando acierte a uno de los tres, imprime "¡Bienvenido al Fandom!" y el programa terminará.
"""
grupo = input("Cual es tu grupo favorito? ")
while grupo != "BTS" and grupo != "BLACKPINK" and grupo != "Stray Kids":
    print("Dame un grupo valido")
    grupo = input("Cual es tu grupo favorito?")
print("¡Bienvenido al Fandom!")