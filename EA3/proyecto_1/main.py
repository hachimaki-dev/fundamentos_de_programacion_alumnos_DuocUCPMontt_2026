def calcular_descuento_medicamentos(edad, trama):
    if edad <= 30:
        if trama in ["A", "B"]:
            return 0.18
        elif trama in ["C", "D"]:
            return 0.12
    elif 31 <= edad <= 60:
        if trama in ["A", "B"]:
            return 0.12
        elif trama in ["C", "D"]:
            return 0.08
            
