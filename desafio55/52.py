sueldo_base = 800000
bonos = {
    'colacion': 50000,
    'movilizacion': 30000
         }
descuentos = {
    'AFP': 0.10,
    'Salud': 0.07
}
total_ingreso = sueldo_base
for monto_bonos in bonos.values():
    total_ingreso += monto_bonos
sueldo_liquido = total_ingreso
for porcentajes in descuentos.values():
    descontado = sueldo_base * porcentajes
    sueldo_liquido -= descontado
print(sueldo_liquido)