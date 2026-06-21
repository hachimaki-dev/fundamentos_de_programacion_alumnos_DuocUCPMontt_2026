def contar_caracteres(texto):
    diccionario = {}
    for letra in texto:
        if letra in diccionario:
            diccionario[letra] += 1
        else:
            diccionario[letra] = 1
    return diccionario
palabra = "hola hoola"
resultado = contar_caracteres(texto=palabra)
print(resultado)