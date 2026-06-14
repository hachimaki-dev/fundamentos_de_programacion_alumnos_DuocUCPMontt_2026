def validar_precio(precio):
    if isinstance(precio(int,float)):
        if precio >= 1000 and precio <= 50000:
            return True
        else:
            return False
    else:
        return False