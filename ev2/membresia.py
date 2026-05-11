#Desarrolle un programa que calcule el valor final de una membresía mensual de gimnasio y el valor final del arriendo de casillero.
#Valores base:
#Membresía: $35.000
#Casillero: $4.500
#Reglas de descuento para la membresía:
#Meses >= 12:
##Plan 1 o 2 → 22%
#Plan 3 o 4 → 15%
#6 <= meses < 12:
#Plan 1 o 2 → 12%
#Plan 3 o 4 → 7%
#Menor a 6 meses → sin descuento.
#Reglas del casillero:
#Plan 1 o 2 → 15% descuento.
#Si además los meses son >= 9 → 5% adicional.
#Debe mostrar ambos valores finales.


membresia = 35000
casillero = 4500

meses = int(input("¿cuantos meses lleva inscrito? :"))
plan = int(input("¿cual es su plan? :"))

if meses >= 12:
    if plan in [1,2] :
        descuento_membresia = 0.22
    else:
        descuento_membresia = 0.15
        
elif meses >= 6:
    if plan in [1,2] :
        descuento_membresia = 0.12
    else:
        descuento_membresia = 0.07
        
else:
    descuento_membresia = 0
    
membresia = membresia * (1 - descuento_membresia)

if plan in [1,2] :
    descuento_casillero = 0.15
    if meses >= 9:
        descuento_casillero = 0.20
else:
     descuento_casillero = 0
        
casillero = casillero * (1 - descuento_casillero)

print(membresia)
print(casillero)
   



        
