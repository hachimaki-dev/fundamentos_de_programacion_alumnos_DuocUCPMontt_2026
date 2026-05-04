sueldo_base = 500000
bono_colacion = 50000
bono_movilizacion = 30000
descuentos_salud = 0.83
#descuento de salud es la suma del 7% por salud y el 10%de AFP

print(f"Hola, su sueldo base es de ${sueldo_base}CLP, tiene un bono de colacion de ${bono_colacion}CLP y uno de movilizacion que es de ${bono_movilizacion}CLP")
print("Para su infortunio a su sueldo base le tenemos que descontar un 7% de salud y un 10% de afp")
sueldo_base = sueldo_base * descuentos_salud
print(f"Su sueldo base quedaria en ${sueldo_base} y su bono de colacion no se toca")
print(f"En total usted recibiria ${sueldo_base + bono_colacion + bono_movilizacion}")