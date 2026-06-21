import random
def generar_password(longitud=8):
    caracteres = "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM1234567890"
    password = ""
    for _ in range(longitud):
        caracteres_al_azar = random.choice(caracteres)
        password += caracteres_al_azar
    return password
print(generar_password())