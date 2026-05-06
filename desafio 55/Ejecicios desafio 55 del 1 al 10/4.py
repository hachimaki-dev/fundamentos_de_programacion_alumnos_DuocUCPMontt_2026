valor_notebook = 1200000
cuotas = 12
costo_envio = 15000

total_por_mes = (valor_notebook / cuotas)

total_mes_con_envio = (total_por_mes + costo_envio)

print("Compraste un notebook por internet y quieres saber cuánto pagarás el primer mes.")

input()

print(f"Como compraste el notebook con 12 cuotas sin interes estrias pagando: {total_por_mes} al mes.")

input()

print(f"Como el envio cuesta 15000$, el primer mes tendras que pagar: {total_mes_con_envio}")