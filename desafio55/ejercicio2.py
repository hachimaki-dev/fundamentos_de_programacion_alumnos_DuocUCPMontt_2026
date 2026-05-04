print("Ejercicio 2: Proyección de ahorro para un auto")
precio_auto = 5000000
dinero_ahorrado = 1500000
ganancia_mensual = 150000

print(f"Tienes ${dinero_ahorrado} ahorrado para comprar un auto de ${precio_auto}, por lo tanto te faltan ${precio_auto - dinero_ahorrado}")
dinero_faltante = precio_auto - dinero_ahorrado
print(f"Cada mes ganas ${ganancia_mensual}")
print(dinero_faltante // ganancia_mensual)