def contar_vocales(palabra : str):
    cont_vocales = 0
    vocales = ["A","E","I","O","U","a","e","i","o","u"]
    for i in palabra:
        if i in vocales:
            cont_vocales += 1
    return cont_vocales