saldo_inicial_tarjeta = 10000
valor_pasaje_micro = 730
valor_metro = 850
recarga = 3000

saldo_tarjeta = saldo_inicial_tarjeta - valor_pasaje_micro
saldo_tarjeta = saldo_tarjeta - (valor_metro * 2)
saldo_final = saldo_tarjeta + recarga

print(f" El saldo final es {saldo_final}")
