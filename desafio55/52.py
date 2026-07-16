sueldo_base = 800000
bonos = {'colacion': 50000, 'movilizacion': 30000}
descuentos = {'AFP': 0.10, 'Salud': 0.07}
descuentos_plata = 0
bonos_total = 0
for i in descuentos.values():
    descuentos_plata = descuentos_plata + (i * sueldo_base)
    print(descuentos_plata)
for i in bonos.values():
    bonos_total = bonos_total + i

sueldo_base = sueldo_base - descuentos_plata + bonos_total
print(sueldo_base)
   