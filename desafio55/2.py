auto = 5000000
ahorrado = 1500000
ahorrado_mensual = 150000

faltante_auto = auto - ahorrado
print(f"Falta {faltante_auto} para conseguir el auto")
meses = faltante_auto // ahorrado_mensual
print(f"la cantidad de meses que debe ahorrar son {meses}")