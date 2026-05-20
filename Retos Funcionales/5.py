def contar_vocales(texto):
    contar_vocales = 0
    for i in texto:
        if i == "a" or i == "e" or i == "i" or i == "e" or i == "u":
            contar_vocales += 1
    return contar_vocales

print(contar_vocales("palabra"))