def es_libro_antiguo(año):
    if año > 1990:
        return True
    else:
        return False

def es_libro_antiguo(anio):
    return anio < 1990

x = es_libro_antiguo(1923)
print(x)