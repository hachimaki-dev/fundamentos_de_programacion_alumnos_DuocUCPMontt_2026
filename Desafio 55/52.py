sueldo_base = 800000

bonos = {"colacion" : 50000,
         "movilizacion" : 30000}

descuentos = {"AFP" : 0.10,
              "Salud" : 0.07}

total_bonos = 0
descuento_total = 0

for bono in bonos.values() :
    total_bonos += bono

for descuento in descuentos.values() :
    descuento_total += descuento

sueldo_base *= (1.0 - descuento_total)
sueldo_total = sueldo_base + total_bonos

print(sueldo_total)