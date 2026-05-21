#Crea contar_caracteres(texto) que retorne un diccionario donde las claves son las letras y los valores son la cantidad de veces que aparecen.

texto = input("Introduce la contraseñas que quieres contar: ")

def contar_caracteres(texto):
    conteo = {}
    for caracter in texto:

        if caracter in conteo:
            conteo[caracter] += 1
        else:
            conteo[caracter] = 1
    return conteo

resultado = contar_caracteres(texto)
print(resultado)