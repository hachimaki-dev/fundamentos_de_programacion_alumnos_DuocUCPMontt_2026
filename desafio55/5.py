saldo_inicial = 10000
valor_micro = 730
valor_metro = 850

recarga = 3000
micros = 1
metro = 2

#micro
saldo_inicial = saldo_inicial - valor_micro
print(saldo_inicial)
#metros
Valor_metro_dia = metro * valor_metro
saldo_inicial = saldo_inicial - Valor_metro_dia
print(saldo_inicial)
#recarga
saldo_inicial = saldo_inicial + recarga
print(saldo_inicial)
