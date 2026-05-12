plan_mensual = 28000
instalacion = 15000
velocidad_usuario = 700
categoria = 1

if velocidad_usuario >=600:
    if categoria == 1 or categoria == 2:
        plan_mensual *= 0.82
        
    if categoria == 3 or categoria == 4:
        plan_mensual *= 0.89
        
elif velocidad_usuario <= 300 >=600:
        if categoria == 1 or categoria == 2:
            
            plan_mensual *= 0.90
        
        if categoria == 3 or categoria == 4:
            plan_mensual *= 0.94
            
        if velocidad_usuario < 300:
            print("sin descuento")
            
if categoria == 1 or categoria == 2:
    instalacion *= 0.80
    
    if velocidad_usuario >= 500:
        instalacion *= 0.90
        
print(plan_mensual)
print(instalacion)
    
        