sueldo_descuento = 0
sueldo_base=50000
bono_colacion = 50000
movilizacion = 30000
sueldo_liquido = 0 
print("--calculadora--")
print(f"Hola , este es su sueldo base : {sueldo_base} , este es su bono de colacion : {bono_colacion} y este es su bono de movilizacion : {movilizacion} ")
sueldo_descuento = (sueldo_base * 100) / 1.7
sueldo_liquido = sueldo_descuento + bono_colacion + movilizacion
print(f"ahora su sueldo liquido es : {sueldo_liquido}")