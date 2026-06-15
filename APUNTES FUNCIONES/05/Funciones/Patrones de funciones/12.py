def tiene_contenido_v1(texto):
    for caracter in texto:
        if caracter != " ":
            return True
    return False