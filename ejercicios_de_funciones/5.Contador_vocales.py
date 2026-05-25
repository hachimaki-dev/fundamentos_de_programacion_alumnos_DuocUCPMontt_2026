def contar_vocales(texto):
    contador = 0
    texto_separado = list(texto)
    for caracter in texto_separado:
        if caracter in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            contador += 1
    return contador
print(contar_vocales("Murcielago"))