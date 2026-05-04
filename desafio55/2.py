valor_auto = 5000000
ahorro_inicial = 1500000
ahorro_mensual = 150000

total_a_ahorrar = valor_auto - ahorro_inicial

total_cuotas = total_a_ahorrar // ahorro_mensual

print(f"El total de cuotas a pagar es: {total_cuotas}")