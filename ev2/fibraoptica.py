plan = 28000 
instalacion = 15000

velocidad = int(input())
categoria = int(input())    

if velocidad >= 600:
    if categoria in [1,2]:
        descuento = 0.18
    else:
        descuento = 0.11
elif velocidad >= 300:
    if categoria in [1,2]:
        descuento = 0.10
    else:
        descuento = 0.06
else:
    descuento = 0
    
plan = plan * (1 - descuento)

if categoria in [1,2]:
    descuento_instalacion = 0.20
    if velocidad >= 500:
        descuento_instalacion = 0.30
    else:
        descuento_instalacion = 0
        
instalacion = instalacion * (1 - descuento_instalacion)

print(plan)
print(instalacion)
    

        
    