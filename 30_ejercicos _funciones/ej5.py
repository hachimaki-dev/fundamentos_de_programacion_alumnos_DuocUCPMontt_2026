def contar_vocales(texto):
    cantidad_vocales = 0
    vocales = "aeiouAEIOU"
    for v in texto:
        if v in vocales:
            cantidad_vocales += 1
    return cantidad_vocales
palabra = input("ingresa una palabra: ")
resultado = contar_vocales(texto=palabra)
print(resultado)