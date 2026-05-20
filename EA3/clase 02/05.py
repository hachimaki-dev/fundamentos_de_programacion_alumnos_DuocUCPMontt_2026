#Crea contar_vocales(texto) que reciba un string y retorne la cantidad de vocales que contiene.

def contar_vocales(texto):
    vocales = "AEIOUaeiou"
    contador =  0
    for vocal in vocales:
        contador += 1
    return contador

print(contar_vocales("Zobeiba"))