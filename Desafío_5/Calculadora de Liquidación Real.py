sueldo_base = 800000

bonos = {
    'colacion': 50000,
    'movilizacion': 30000
}

descuentos = {
    'AFP': 0.10,
    'Salud': 0.07
}

sueldo_final = sueldo_base

for bono in bonos.values():

    sueldo_final += bono


for descuento in descuentos.values():

    descuento_dinero = sueldo_base * descuento

    sueldo_final -= descuento_dinero

print("Sueldo líquido final:", sueldo_final)