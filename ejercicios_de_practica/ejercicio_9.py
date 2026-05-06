valor_de_polera = 15000
costo_de_tela = 4000
costo_de_estampado = 2500
costo_de_empaque = 500

costo_de_produccion = (costo_de_tela + costo_de_estampado + costo_de_empaque) * 50
ganancias = (valor_de_polera * 50) - (costo_de_produccion)
print(ganancias)