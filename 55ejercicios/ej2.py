# Ejercicio 2: Proyección de Ahorro para un Auto 🚗

print("Sistema de Ahorro para comprar TU auto")
print("--------------------------------------")

precio_auto = 5000000
ahorro_actual = 1500000
ahorro_mensual = 150000

dinero_faltante = precio_auto - ahorro_actual

meses = dinero_faltante // ahorro_mensual

print(meses)