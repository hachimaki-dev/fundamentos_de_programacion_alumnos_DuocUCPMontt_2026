def validar_año(año):
    if isinstance(año, int):
        if año > 0 and año <= 2026: 
            return True
        else:
            return False
    else:
        return False
def validar_año_try(año):
    try:
        año_entero = int(año)
        if año_entero >0 and año_entero <= 2026:
            return True
        else: 
            return False
    except:
        return False