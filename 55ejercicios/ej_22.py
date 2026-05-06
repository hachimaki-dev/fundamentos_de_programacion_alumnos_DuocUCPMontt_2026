# Ejercicio 22: Ahorro Meta Mensual (PS5)

print("===========================")
print("Simulador de ahorro mensual")
print("===========================")

ahorro = 0
ahorro_mensual = 80000
precio_ps5 = 450000
meses = 0

while ahorro < precio_ps5:
    ahorro = ahorro + ahorro_mensual
    meses = meses + 1

print(meses)