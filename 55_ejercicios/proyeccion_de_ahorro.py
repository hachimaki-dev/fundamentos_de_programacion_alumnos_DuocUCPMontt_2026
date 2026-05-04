precio_auto = 5000000
total_ahorrado = 1500000
print(f"Actualmente faltan: ${precio_auto - total_ahorrado} pesos")
faltante = precio_auto - total_ahorrado
meses = faltante // 15000
print(f"Suponiendo que cada mes ahorras $15000, tendrías que ahorrar durante: {meses} meses")