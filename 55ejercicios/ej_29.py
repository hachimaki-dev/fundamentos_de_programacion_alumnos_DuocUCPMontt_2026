# Ejercicio 29: Simulación de Trote (Apple Watch)

print("=====================")
print("Simulador de calorías")
print("=====================")

meta = 300

calorias = 0
minutos = 0

while calorias < meta:

    minutos = minutos + 1

    if minutos <= 10:
        calorias = calorias + 20

    else:
        calorias = calorias + 10

print(minutos)