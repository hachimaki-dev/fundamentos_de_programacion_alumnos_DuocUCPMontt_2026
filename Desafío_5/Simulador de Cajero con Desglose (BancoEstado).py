monto = 37000

billetes = [20000, 10000, 5000, 1000]

resultado = {}

for billete in billetes:

    cantidad = monto // billete

    resultado[billete] = cantidad

    monto = monto % billete

print(resultado)