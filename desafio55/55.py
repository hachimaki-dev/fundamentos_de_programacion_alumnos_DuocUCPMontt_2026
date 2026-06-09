giro = 37000
billetes = [20000, 10000, 5000, 1000]
monto_a_sacar = {}
for billete in billetes:
    cantidad_de_billetes = giro // billete
    monto_a_sacar[billete] = cantidad_de_billetes
    giro -= billete
print(monto_a_sacar)