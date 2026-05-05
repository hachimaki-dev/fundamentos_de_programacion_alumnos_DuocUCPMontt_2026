valor_venta_polera=15000

costo_tela=4000
costo_estampado=2500
costo_empaque=500
venta_x_mes=50

costo_hacer_polera=costo_tela+costo_estampado+costo_empaque

ganancia_x_polera=valor_venta_polera-costo_hacer_polera

ganancia_mensual=ganancia_x_polera*venta_x_mes

print(f"${ganancia_mensual} es tu ganancia mensual")
