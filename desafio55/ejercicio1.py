print("Ejercicio número 1: Liquidación de sueldo básico.")

sueldo_base = 500000
bono_colacion = 50000
transporte = 30000

print(f"Tienes un sueldo base de {sueldo_base}, recibes un bono de {bono_colacion} para colación y también recibes {transporte} para transporte.")
print("Se te descontaran un 7% del sueldo base por salud y un 10% por AFP.")

sueldo_liquido = sueldo_base

sueldo_liquido -= sueldo_base * 0.07
sueldo_liquido -= sueldo_base * 0.10

sueldo_liquido += bono_colacion
sueldo_liquido += transporte
print(sueldo_liquido)