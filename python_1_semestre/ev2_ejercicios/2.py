""" Membresía de Gimnasio
Desarrolle un programa que calcule el valor final de una membresía mensual 
y el valor final del arriendo de casillero.

Valores base:
Membresía: $35.000
Casillero: $4.500
Reglas:
Meses >= 12:
Plan 1 o 2 → 22%
Plan 3 o 4 → 15%
6 <= meses < 12:
Plan 1 o 2 → 12%
Plan 3 o 4 → 7%
Menor a 6 meses → sin descuento.
Casillero:
Plan 1 o 2 → 15%.
Si además los meses son >= 9 → 5% adicional."""

membresia = 35000
casillero = 4500
total = 0

print(f"la membresia mensual cuesta: {membresia}")
print(f"el casillero cuesta: {casillero}")

while True:
    meses = int(input("ingrese los meses que cotiza: "))
    plan = input("ingrese el plan que desea: 1 o 2 o 3 o 4?")
    
    if meses >= 12 and plan == "1" or "2":
        total = membresia * meses 
        total = total - (total * 0.22)
        total = total + casillero
        total = total - (casillero * 0.15)

    elif meses >= 12 and plan == "3" or "4":
        total = membresia * meses  
        total = total - (total * 0.15)
        total = total + casillero
        total = total - (casillero * 0.15)

    elif meses >=6 and meses < 12 and plan == "1" or "2":
        total = membresia * meses 
        total = total - (total * 0.12)
    
    elif meses >=6 and meses < 12 and plan == "3" or "4":
        total = membresia * meses
        total = total - (total * 0.07)
    
    elif meses < 6 and plan == "1" or "2" or "3" or "4":
        total = membresia * meses + casillero