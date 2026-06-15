def es_libro_antiguo(anio):
    if anio < 1990:
        return True
    else:
        return False

# Pruebas
print(es_libro_antiguo(1985))  # Devuelve True
print(es_libro_antiguo(2005))  # Devuelve False