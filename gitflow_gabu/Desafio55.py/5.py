micro = 730
metro = 850
recarga = 3000

saldo_bip = 10000
saldo_bip -= micro
saldo_bip -= metro * 2
saldo_bip += recarga

print("EL saldo que te queda es: ", saldo_bip)