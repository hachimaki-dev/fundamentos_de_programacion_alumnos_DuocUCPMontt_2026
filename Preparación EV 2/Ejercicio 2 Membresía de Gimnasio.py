# Ejercicio 2: Membresía de Gimnasio
# MEDIUM
# Desarrolle un programa que calcule el valor final de una membresía mensual de gimnasio y el valor final del arriendo de casillero.

# Valores base:
# Membresía: $35.000
# Casillero: $4.500
# Reglas de descuento para la membresía:

# Meses >= 12:
# Plan 1 o 2 → 22%
# Plan 3 o 4 → 15%
# 6 <= meses < 12:
# Plan 1 o 2 → 12%
# Plan 3 o 4 → 7%
# Menor a 6 meses → sin descuento.
# Reglas del casillero:

# Plan 1 o 2 → 15% descuento.
# Si además los meses son >= 9 → 5% adicional.
# Debe mostrar ambos valores finales.

# Input Esperado
# 12
# 1

# Output Esperado
# Membresia: 27300
# Casillero: 3633

membresia = 35000
casillero = 4500

meses = int(input("¿Cuántos meses contratará?: "))
plan = input("Plan (1, 2, 3 o 4): ")

descuento_menbresia = 0

if meses >= 12:
    descuento_membresia = 0.22 if plan in ["1", "2"] else 0.15

elif meses >= 6:
    descuento_membresia = 0.12 if plan in ["1", "2"] else 0.07

membresia_final = membresia * (1 - descuento_membresia)

descuento_casillero = 0

if plan in ["1", "2"]:
    descuento_casillero = 0.15

    if meses >= 9:
        descuento_casillero += 0.05

casillero_final = casillero * (1 - descuento_casillero)

print(f"Membresia: {int(membresia_final)}")
print(f"Casillero: {int(casillero_final)}")