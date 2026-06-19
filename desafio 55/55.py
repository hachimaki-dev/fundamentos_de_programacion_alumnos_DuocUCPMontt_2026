retiro = 37000

billetes = [20000, 10000, 5000, 1000]

desglose = {}

for denominacion in billetes:
    
    cantidad = retiro // denominacion
    
    desglose[denominacion] = cantidad
    
    retiro = retiro % denominacion

print(desglose)