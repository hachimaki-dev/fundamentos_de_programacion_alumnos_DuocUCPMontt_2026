def es_nota_valida(nota):
    return isinstance(nota, (int, float)) and 1.0 <= nota <= 7.0
#isinstance(valor, tipo) retorna True si valor es del tipo indicado. La tupla (int, float) permite entero o decimal.
# 1.0 <= nota <= 7.0 es una «comparación encadenada» = nota >= 1.0 and nota <= 7.0