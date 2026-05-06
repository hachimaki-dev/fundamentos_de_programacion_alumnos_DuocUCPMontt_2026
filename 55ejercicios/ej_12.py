# Ejercicio 12: Aprobación de Crédito (AND simple)

print("==============================================")
print("Bienvenido al sistema de evaluación de crédito")
print("==============================================")

sueldo = 550000
deudas = 1

if sueldo > 500000 and deudas == 0:
    print("Aprobado")
else:
    print("Rechazado")