sueldo_base= 500000
bono_colacion= 50000
bono_movilizacion= 30000
#se descuenta 7% por salud y otro 10% por AFP
descuentos= 17

sueldo= sueldo_base - (sueldo_base*descuentos /100)
sueldo_liquido= sueldo + bono_colacion + bono_movilizacion

print(f"Este es tu sueldo liquido {sueldo_liquido}")