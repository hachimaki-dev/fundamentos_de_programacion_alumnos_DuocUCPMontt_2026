mensualidad = 85000
kit_material = 18000
edad_usuario_meses = 10
nivel = 2

# Lógica de Mensualidad
if edad_usuario_meses <= 18:
    if nivel == 1 or nivel == 2:
        mensualidad *= 0.80 
        
    elif nivel == 3: 
        mensualidad *= 0.82 
        
elif 19 <= edad_usuario_meses <= 36:
    if nivel == 1 or nivel == 2:
        mensualidad *= 0.88 
        
    elif nivel == 3 or nivel == 4:
        mensualidad *= 0.93 

else:
    print("Sin descuento en mensualidad.")


if nivel == 1 or nivel == 2:
    kit_material *= 0.90 
    
    if edad_usuario_meses <= 12:
        kit_material *= 0.95 
        
print(mensualidad)
print(kit_material)
      
        

