Sueldo_Base = 500000
Bono_Colacion = 50000
Bono_Movilizacion = 30000


Descuento_Salud = Sueldo_Base * 0.07
Descuento_AFP = Sueldo_Base * 0.10

Sueldo_Liquido = Sueldo_Base + Bono_Colacion + Bono_Movilizacion - (Descuento_AFP + Descuento_Salud)

print (f"Su sueldo liquido es {Sueldo_Liquido}")
