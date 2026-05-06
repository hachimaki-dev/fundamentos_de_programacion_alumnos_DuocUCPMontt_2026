monto = 37000
billetes = {20000: 0, 10000: 0, 5000: 0, 1000: 0}

for billete in billetes:
    billetes[billete] = monto // billete
    monto %= billete

print(billetes)