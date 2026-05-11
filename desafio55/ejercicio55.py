print("el cliente quiere queque, pero aparte quiere sacar 37 lucas")
billetes = [20000, 10000, 5000, 1000]
monto = 37000

disionario = {}

for billete in billetes:
    if monto >= billete:
        cantidad = monto // billete
        disionario[billete] = cantidad
        monto = monto % billete


print(disionario)