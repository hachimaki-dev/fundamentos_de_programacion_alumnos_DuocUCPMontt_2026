retiro = 37000
billetes = [20000, 10000, 5000, 1000]
resultado = {}
for b in billetes:
    cantidad = retiro // b
    resultado[b] = cantidad
    retiro = retiro % b
print(resultado) 