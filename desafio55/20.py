saldo_usario = 50000
limite_diario = 200000
retiro= 60000

regla_1 = False
regla_2 = False
regla_3 = False

# regla 1: Si lo que pides es más que tu límite diario, rechaza con 'Excede límite diario'. 

if retiro >limite_diario:
    print("excediste limite dario")
    
    regla_1 = True
    
# regla 2: Si pides más de lo que tienes en el saldo, rechaza con 'Saldo insuficiente'.  
    
elif retiro > saldo_usario :
    print("saldo insuficiente")
    
    regla_2 = True    
    
# Regla 3: Si lo que pides no es múltiplo de 5000 (el cajero no da monedas), rechaza con 'Monto inválido'. Si pasas todas las reglas, 'Retiro exitoso'.    
    
elif retiro %5000 == 0:
    print("si puede sacar dinero porque es multiple")
else:
    print("retiro ")