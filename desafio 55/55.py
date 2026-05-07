# 1. Datos Iniciales
monto_a_retirar = 37000
billetes_disponibles = [20000, 10000, 5000, 1000] 
resultado = {} 


monto_restante = monto_a_retirar


for billete in billetes_disponibles:
    
    cantidad_billetes = monto_restante // billete
    
    
    if cantidad_billetes > 0:
        resultado[billete] = cantidad_billetes
        
        
        monto_restante = monto_restante % billete


print(f"Desglose para ${monto_a_retirar}:")
print(resultado)
