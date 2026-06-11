def es_libro_antiguo(año):
    if año < 1990:
        return True
    else:
        return False
print(es_libro_antiguo(2008))
def es_libro_antiguo_short(año):
    return año < 1990
print(es_libro_antiguo_short(1960))