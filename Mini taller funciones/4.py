def es_libro_antiguo(anio):
    return True if anio < 1990 else False    #DE MANERA SIMPLE: Retorna True SI anio < 1990 sino False
a = es_libro_antiguo(1991)
b = es_libro_antiguo(1890)
print(f"{a} | {b}")
