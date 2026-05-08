# Datos Iniciales
sueldo_base = 800000
bonos = {'colacion': 50000, 'movilizacion': 30000}
descuentos_porcentaje = {'AFP': 0.10, 'Salud': 0.07}

# 1. Sumar los bonos al sueldo base
# Iniciamos el total con el sueldo base
sueldo_liquido = sueldo_base

for monto_bono in bonos.values():
    sueldo_liquido += monto_bono

# 2. Calcular y restar los descuentos legales
# Los descuentos se aplican SÓLO sobre el sueldo base
for porcentaje in descuentos_porcentaje.values():
    monto_a_descontar = sueldo_base * porcentaje
    sueldo_liquido -= monto_a_descontar

# Resultado final
print(f"El sueldo líquido final es: ${sueldo_liquido:,.0f}")