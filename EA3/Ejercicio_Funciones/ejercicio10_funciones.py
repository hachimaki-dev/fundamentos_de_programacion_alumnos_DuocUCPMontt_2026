def validar_stock(cantidad):
    if isinstance(cantidad, int):
        if cantidad >= 0:
            return True
        else:
            return False
    else: 
        return False