'''Ejercicio 2: Membresía de Gimnasio
MEDIUM
Desarrolle un programa que calcule el valor final de una membresía mensual de gimnasio y el valor final del arriendo de casillero.

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
Debe mostrar ambos valores finales.'''

membresia = 35000
casillero = 4500
descuento_casillero = 0
descuento_membresia = 0
meses = int(input("Ingrese la cantidad de meses: "))
plan = int(input("Ingrese su plan: "))

if meses >= 12:
    if plan == 1 or 2:
        descuento_membresia = membresia * 0.22
        membresia -= descuento_membresia
    else:
        descuento_membresia = membresia * 0.15
        membresia -= descuento_membresia
elif 6 <= meses < 12:
    if plan == 1 or 2:
        descuento_membresia = membresia * 0.12
        membresia -= descuento_membresia
    else:
        descuento_membresia = membresia * 0.07
        membresia -= descuento_membresia

if plan == 1 or 2:
    descuento_casillero = casillero * 0.15
    casillero -= descuento_casillero
    if meses >= 9:
        descuento_casillero = casillero * 0.05
        casillero -= descuento_casillero
        
print(int(membresia))
print(int(casillero))
