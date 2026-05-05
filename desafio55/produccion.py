
# Datos Iniciales: Vendes cada polera a 15000. Hacer una polera te cuesta: 4000 la tela, 2500 el estampado y 500 el empaque. Vendiste 50 poleras en el mes.
#  La ganancia por cada polera es su precio de venta menos todo lo que te costó hacerla. La ganancia del mes es esa ganancia por unidad multiplicada por las poleras que vendiste.

venta_poleron = 15000 
hacer_poleron = 4000
tela = 2500
empaque = 500
precio_poleron = hacer_poleron + tela + empaque
print(f" vendiste 50 polerones este mes cada uno vale {venta_poleron} mil pesos .pero te cuesta hacerlos {precio_poleron}")
ganacia_individual = venta_poleron - precio_poleron
ganacia_mes = ganacia_individual * 50
print(f"tu ganancia por poleron es de {ganacia_individual} mil pesos y tu ganancia por los 50 polerones del mes es de {ganacia_mes}")















