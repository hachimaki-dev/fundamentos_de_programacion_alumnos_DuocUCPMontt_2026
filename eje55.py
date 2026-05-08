monto_solicitado = int(input("¿Cuánto dinero deseas sacar? "))
billetes = [20000, 10000, 5000, 1000]
desglose = {}
 
for billete in billetes:
    cantidad = monto_solicitado // billete
    if cantidad > 0:
        desglose[billete] = cantidad
    monto_solicitado = monto_solicitado % billete
 
print(desglose)