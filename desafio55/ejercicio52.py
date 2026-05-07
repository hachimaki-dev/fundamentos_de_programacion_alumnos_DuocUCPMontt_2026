sueldo_base = 800000
sueldo_bruto = 0
bonos = {"colación": 50000, "transporte": 30000}
descuentos = {"AFP": 0.10, "salud": 0.07}
descuentillos = 0
sueldo_liquido = 0

for i in bonos.values():
    sueldo_bruto = sueldo_base + i

print(sueldo_base)

for i in descuentos.values():
    descuentillos = sueldo_base * i
    sueldo_liquido = sueldo_base - descuentillos
print(sueldo_liquido)

#estudiarlo en casa, con este me confundi mucho.