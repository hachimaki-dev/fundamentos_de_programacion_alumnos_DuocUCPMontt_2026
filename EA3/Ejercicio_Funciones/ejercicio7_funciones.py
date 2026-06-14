def tiene_contenido_v1(texto):
    for caracter in texto:
        if caracter != " ":
            return True
        else:
            return False
def tiene_contenido_v2(texto):
    if texto.lstrip() != "":
        return True
    else:
        return False
resultado1 = tiene_contenido_v2("Don Quijote")
print(resultado1)
