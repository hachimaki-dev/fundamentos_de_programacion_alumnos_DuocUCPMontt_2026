def contar_vocales(texto):
    lista_de_vocales = "a","e","i","o","u"
    vocales = 0
    for i in texto:
        if i in lista_de_vocales:
            vocales += 1
    return vocales

print(contar_vocales("paralelipedo"))