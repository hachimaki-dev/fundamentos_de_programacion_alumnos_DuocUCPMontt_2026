def contar_caracteres(texto):
    diccionario = {}
    for i in texto:
        letra = i
        contador_letra = texto.count(i)
        diccionario.setdefault(i,contador_letra)
    return diccionario