#Crea contar_vocales(texto) que reciba un string y retorne la cantidad de vocales que contiene.

def contar_vocales(texto):
    contador = 0

    for letra in texto:
        if letra in "aeiouAEIOU":
            contador += 1
    
    return contador

print(contar_vocales("Hola mundo"))