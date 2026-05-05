saldo_inicial = 10000
valor_micro = 730
valor_metro = 850
recarga = 3000
pasaje_dia = valor_micro + (valor_metro * 2)
saldo_diario = (saldo_inicial - pasaje_dia) + recarga
print(saldo_diario)