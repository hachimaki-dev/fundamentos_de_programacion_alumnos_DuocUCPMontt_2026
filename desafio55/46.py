ventas = {"LocalA": 150, "LocalB" : 300, "LocalC" : 100}
plata_ganada = 0 
for plata in ventas.values():
    plata_ganada += plata
    print(plata_ganada)