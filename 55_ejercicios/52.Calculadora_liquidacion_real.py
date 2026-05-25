sueldo_base = 800000
porcentaje_descuentos = 0


bonos = {
    'colacion' : 50000,
    'movilizacion' : 30000
}
descuentos = {
    'afp' : 0.10,
    'salud' : 0.07
}

for desc in descuentos.values():
    porcentaje_descuentos += desc
sueldo_liquido = sueldo_base - (sueldo_base * porcentaje_descuentos)

for bono_especifico in bonos.values():
    sueldo_liquido += bono_especifico
sueldo_final = sueldo_liquido

print(sueldo_final)