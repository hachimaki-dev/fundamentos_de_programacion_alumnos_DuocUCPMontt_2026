def es_libro_antiguo(año):
    if año < 1990:
        return True
    else:
        return False
resultado = es_libro_antiguo(1991)
print(resultado)