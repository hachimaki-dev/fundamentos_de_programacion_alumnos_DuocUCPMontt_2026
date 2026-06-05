def contar_vocales(vocal):
    contador_vocal = 0
    vocales = ['a','A','E','e','I','i','O','o','u','U']
    for i in vocal:
        if i in vocales:
            contador_vocal += 1
    return contador_vocal
resultado = contar_vocales(input('Introduzca Una Palabra:\n'))
print(resultado)
    