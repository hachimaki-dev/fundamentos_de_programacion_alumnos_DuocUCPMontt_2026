def es_libro_antiguo(anio):
    #es lo mismo devuelve true si es verdadero y False cuando no se cumple la condición
    return anio < 1990
    
    #if anio < 1990:
    #    return True
    #else:
    #    return False
    
print(es_libro_antiguo(1985))
print(es_libro_antiguo(2005))