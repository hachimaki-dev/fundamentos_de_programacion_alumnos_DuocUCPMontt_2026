# 🎤 Reto 2: Bias K-Pop Validator
# Crea un programa que te pregunte a qué grupo quieres unirte. Solo te dejará pasar si ingresas nombres de grupos válidos.

# Instrucciones:

# El usuario debe ingresar el nombre de su grupo favorito.
# Mientras el grupo no sea "BTS" y no sea "BLACKPINK" y no sea "Stray Kids", el programa seguirá pidiendo un grupo válido. (Ojo: usa combinación de and u or con !=).
# Cuando acierte a uno de los tres, imprime "¡Bienvenido al Fandom!" y el programa terminará.

grupo_favorito = ""

print("----- Bias K-Pop Validator -----")

while grupo_favorito != "BTS" and grupo_favorito != "BLACKPINK" and grupo_favorito != "STRAY KIDS":
    grupo_favorito = input("Ingrese su grupo favorito de K-Pop: ").upper()

print("¡Bienvenido al Fandom!")

# while True:
#     grupo_favorito = input("Ingrese su grupo favorito de K-Pop: ").upper()
#     if grupo_favorito == "BTS" or grupo_favorito == "BLACKPINK" or grupo_favorito == "STRAY KIDS":
#         print("¡Bienvenido al Fandom!")
#         break
