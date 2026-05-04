sueldo_base = 500000
bono_colacion = 50000
bono_movilizacion = 30000

# Salud y AFP
sueldo_base = sueldo_base * 0.83

# Sueldo + bonos
sueldo_base = sueldo_base + bono_colacion + bono_movilizacion

print(sueldo_base)