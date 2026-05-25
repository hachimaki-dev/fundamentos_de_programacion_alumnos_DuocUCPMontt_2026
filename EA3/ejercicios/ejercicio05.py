#Crea contar_vocales(texto) que reciba un string y retorne la cantidad de vocales que contiene.

def contar_vocales(texto):
    contadorvocales = 0
    vocales = ['a','A','e','E','i','I','o','O','u','U']
    for i in texto:
        if i in vocales:
            contadorvocales +=1 
    return contadorvocales

resultado = contar_vocales(input('Introduzca una palabra: '))

print (resultado)