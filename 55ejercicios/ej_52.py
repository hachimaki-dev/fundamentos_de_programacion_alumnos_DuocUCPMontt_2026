# Ejercicio 52: Calculadora de Liquidación Real

print("============================")
print("Sistema de cálculo de sueldo")
print("============================")

sueldo_base = 800000

bonos = {'colacion': 50000, 'movilizacion': 30000}

descuentos = {'AFP': 0.10, 'Salud': 0.07}

total = sueldo_base

for bono in bonos.values():
    total = total + bono

for porcentaje in descuentos.values():
    descuento = sueldo_base * porcentaje
    total = total - descuento

print(total)