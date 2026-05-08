contador_fallido = 0
clave = "secreto"
clave_ingresada = "hola"

while contador_fallido >= 3:
    if clave_ingresada != clave:
        contador_fallido = contador_fallido + 1
print(contador_fallido)

