membresia = 35000
casillero = 4500
meses = 12
plan = '1'

if meses >= 12:
    if plan == '1' or plan == '2':
        membresia *= 0.78
        
    elif plan == '1' or plan == '4':
        membresia *= 0.85
        
elif meses >= 6 <= 12:
    if plan == '1' or plan == '2':
        membresia *= 0.88
        
    elif plan == '3' or plan == '4':
        membresia *= 0.93
        
    elif meses < 6:
        print("sin descuento")
        
if plan == '1' or plan == '2':
    casillero *= 0.85
    
    if meses >= 9:
       casillero *= 0.95
    
print(membresia)
print(casillero)
    
    
        