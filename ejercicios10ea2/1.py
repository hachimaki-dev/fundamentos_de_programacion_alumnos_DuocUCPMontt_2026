cuenta_mensual = 45000
carga_medicion = 6000
consumo = 600
grupo = "b"

if consumo >= 500:
    if grupo == 'a' or grupo == 'b':
        cuenta_mensual *= 0.8
        
    elif grupo == 'c' or grupo == 'd':
        cuenta_mensual *= 0.86
        
elif consumo >= 200 >= 499:
    
    if grupo == 'a' or grupo == 'b':
        cuenta_mensual *=  0.12
        
    elif grupo == 'c' or grupo == 'd':
        cuenta_mensual *= 0.92
        
    elif consumo < 200:
        print("sin descuento")
    
if grupo == 'a' or grupo == 'b':
    carga_medicion *= 0.9
    
    if consumo >= 400:
        carga_medicion *= 0.95
        
print(f"Cuenta energia: {cuenta_mensual}\nCargo Medición: {carga_medicion}")

        
        
        
    
    
        
    
        
    
    



