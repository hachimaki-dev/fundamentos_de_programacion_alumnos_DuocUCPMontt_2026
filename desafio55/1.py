sueldo_base = 500000
bono_colacion = 50000
movilizacion = 30000  
descuento_fonasa = sueldo_base * 0.07
descuento_afp = sueldo_base * 0.1
sueldo_base = sueldo_base - descuento_afp - descuento_fonasa
nuevo_sueldo = bono_colacion + movilizacion + sueldo_base
print(f"El sueldo liquido es {nuevo_sueldo}")