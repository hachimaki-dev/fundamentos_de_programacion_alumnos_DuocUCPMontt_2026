monto_compra = 25000
destino = 'Magallanes'

if monto_compra > 20000:
    
    costo_envio = 0
else:
    
    costo_envio = 3000
if destino == 'Magallanes' or destino == 'Aysen':
    
    costo_envio += 2000

print(costo_envio)