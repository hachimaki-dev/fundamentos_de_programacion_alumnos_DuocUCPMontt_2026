"""
Ejercicio 2: Membresía de Gimnasio
MEDIUM
Desarrolle un programa que calcule el valor final de una membresía mensual 
de gimnasio y el valor final del arriendo de casillero.

Valores base:

Membresía: $35.000
Casillero: $4.500
Reglas de descuento para la membresía:

Meses >= 12:
Plan 1 o 2 → 22%
Plan 3 o 4 → 15%
6 <= meses < 12:
Plan 1 o 2 → 12%
Plan 3 o 4 → 7%
Menor a 6 meses → sin descuento.

Reglas del casillero:
Plan 1 o 2 → 15% descuento.

Si además los meses son >= 9 → 5% adicional.
Debe mostrar ambos valores finales.

Input Esperado
12
1

Output Esperado
Membresia: 27300
Casillero: 3633
"""

valor_membresia = 35000
valor_casillero = 4500
descuento_membresia = 0

plan = int(input("---Bienvenidx a la membresia del gimnasio---\n" \
"Para 12 meses o mas: Plan 1 o 2 → 22%, Plan 3 o 4 → 15%\n"
"Entre 6 a 12 meses: Plan 1 o 2 → 12%, Plan 3 o 4 → 7%\n"
"Menor a 6 meses: No hay descuento\n"
"Porfavor elija un plan (1, 2, 3 o 4): "))
meses = int(input("Para cuantos meses quiere la membresia: "))

if meses >=12:
    if plan == 1 or plan == 2:
        descuento_membresia = 0.22 
    elif plan == 3 or plan == 4:
        descuento_membresia = 0.15
if 6 <= meses < 12:
    if plan == 1 or plan == 2:
        descuento_membresia = 0.12 
    elif plan == 3 or plan == 4:
        descuento_membresia = 0.07
else:
    descuento_membresia = 0

total_membresia = valor_membresia * (1 - descuento_membresia)

total_casillero = valor_casillero

if plan == 1 or plan == 2:
    total_casillero = 0.85
    if meses >= 9:
        total_casillero = 0.95

print(f"Membresia: {total_membresia}")
print(f"Casilero: {total_casillero}")





