print("Liquidación de Remuneración \n Mes: mayo 2026 \n -Benjamin Valenzuela \n")

sueldo_base = 500000
bono_movilizacion = 30000
bono_colacion = 50000

print(f"Este es su liquidación total(bruto)\n - {sueldo_base + bono_movilizacion + bono_colacion}")

desuento = sueldo_base * 0.17

bono_total = bono_colacion + bono_movilizacion

print(f"Este es el sueldo liquido \n - {sueldo_base + bono_total - desuento}")

