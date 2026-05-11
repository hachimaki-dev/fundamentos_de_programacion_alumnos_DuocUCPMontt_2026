# Ejercicio 50: Imprimir Boleta Detallada

print("================================================")
print("Bienvenido al sistema de boletas del restaurante")
print("================================================")

cuenta = {'Papas': 5000, 'Pizza': 10000}

total = 0

for plato, precio in cuenta.items():
    total = total + precio

propina = total * 0.10
total_final = total + propina

print("Total final:", total_final)