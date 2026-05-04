# Ejercicio 1 Liquidacion de Sueldo Basico 🏦💰

print("Sistema de Sueldo de Liquidacion")
print("Bienvenido al sistema")


sueldo_base = 500000
colacion = 50000
movilizacion = 30000

salud = sueldo_base * 0.07
afp = sueldo_base * 0.10

total_descuentos = salud + afp
sueldo_liquido = sueldo_base + colacion + movilizacion - total_descuentos

print("El sueldo líquido es:")
print(sueldo_liquido)