auto = 5000000
ahorrado = 1500000
ahorrar_cada_mes = 150000

total_ahorrar = auto - ahorrado
total_cuotas = total_ahorrar // ahorrar_cada_mes

print(f"el total de cuotas es de:{total_cuotas}")