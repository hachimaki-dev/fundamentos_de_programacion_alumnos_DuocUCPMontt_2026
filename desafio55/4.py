notebook = 1200000
cuotas = 12
valor_envio = 15000
#valor cuota
valor_cuota = notebook // cuotas
valor_cuota_con_envio = valor_cuota + valor_envio

print(f"El valor de la primera cuota con envio es de {valor_cuota_con_envio}")