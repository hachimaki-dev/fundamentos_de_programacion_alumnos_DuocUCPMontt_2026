retiro = 37000
billetes = [20000, 10000, 5000, 1000]
resultado = {}
for denominacion in billetes:
    cantidad = retiro // denominacion
    if cantidad > 0:
        resultado[denominacion] = cantidad
        retiro = retiro % denominacion
print(resultado)