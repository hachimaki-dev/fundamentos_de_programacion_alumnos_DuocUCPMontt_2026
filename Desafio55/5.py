saldo = 10000

pasaje_micro = 730
pasaje_metro = 850

recarga = 3000

saldo -= pasaje_micro + (pasaje_metro * 2)
saldo += recarga

print(saldo)