valor_notebook = 1200000
envio = 15000
cuotas = 12
plata_a_pagar_x_mes = valor_notebook / cuotas
plata_pagada = 0

valor_primera_cuota = plata_a_pagar_x_mes + envio

print (f"el valor de su primera cuota es de mas el envio es de {valor_primera_cuota}")