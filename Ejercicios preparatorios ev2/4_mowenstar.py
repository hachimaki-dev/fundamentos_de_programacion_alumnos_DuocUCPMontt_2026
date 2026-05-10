velocidad = 700
categoria = 1
planmensual=28000
instalacion=15000


if velocidad >= 600:
    if categoria == 1 or categoria == 2:
        planmensual -= planmensual*0.18
    elif categoria == 3 or categoria == 4:
        planmensual -= planmensual*0.11
elif 300 <= velocidad < 600:
    if categoria == 1 or categoria == 2:
        planmensual -= planmensual*0.1
    elif categoria == 3 or categoria == 4:
        planmensual -= planmensual*0.06
else:
    planmensual=planmensual 

#instalacion

if categoria == 1 or categoria == 2:
    instalacion -= instalacion*0.2
    if velocidad >= 500:
        instalacion -= instalacion*0.1
                  
print(f'El valor de su plan mensual es ${int(planmensual)}') 
print(f'Su cargo de instalacion es ${int(instalacion)}')
                