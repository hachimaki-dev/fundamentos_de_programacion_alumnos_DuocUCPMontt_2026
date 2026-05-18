sueldo_base = 500000

bono_colacion = 50000   

bono_movilizacion = 30000

descuentos_Salud = sueldo_base * 0.07

descuento_AFP = sueldo_base * 0.10

sueldo_liquido = sueldo_base - descuentos_Salud - descuento_AFP + bono_colacion + bono_movilizacion

print(f"su sueldo base es de {sueldo_base} \n bono de colacion {bono_colacion} \n bono de movilizacion {bono_movilizacion} \n sueldo final {sueldo_liquido}")