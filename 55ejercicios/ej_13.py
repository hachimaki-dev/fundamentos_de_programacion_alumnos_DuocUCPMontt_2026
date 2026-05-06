# Ejercicio 13: Promoción VIP BancoEstado

print("=======================================")
print("Bienvenido al sistema de evaluación VIP")
print("=======================================")

sueldo = 800000
anios_banco = 6
deudas = 0

if sueldo > 1000000 or (anios_banco >= 5 and deudas == 0):
    print("Cliente VIP")
else:
    print("Cliente Normal")