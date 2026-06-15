def tiene_contenido_v1(texto):
    for letra in texto:
        if letra != " ":
            return True
        else:
            return False

def tiene_contenido_v2(texto):
    if texto.strip() != " ":
        return True
    else:
        return False

libro = tiene_contenido_v1("Don Quixote")
libro2 = tiene_contenido_v2("   don quixote   ")
print(libro)
print(libro2)