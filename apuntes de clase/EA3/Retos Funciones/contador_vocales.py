def contador_vocales(texto):
    vocales = "aeiou"
    contador = 0
    for letra in texto:
        if letra.lower() in vocales:
            contador += 1
    return print(f"{texto} tiene {contador} vocales")

contador_vocales(input("Ingresa un texto: "))