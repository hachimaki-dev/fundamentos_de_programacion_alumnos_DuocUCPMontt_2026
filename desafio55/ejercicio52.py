sueldo_base = 800000
bonos = {"colacion": 50000,
         "movilizacion": 30000}
descuentos = {"AFP": 0.10,
              "Salud": 0.07}
bonos_total = 0
descuento = 0
for i in bonos.values():
    bonos_total += i
for x in descuentos.values():
    descuento = sueldo_base * x
    sueldo_liquido_total = sueldo_base - descuento
print(sueldo_liquido_total)

    
    





