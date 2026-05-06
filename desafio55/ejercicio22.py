alcancia = 0
ahorro_mes = 80000
precio_consola = 450000
meses = 0

while alcancia <= precio_consola:
    alcancia += ahorro_mes
    meses += 1
    print(f"Mes {meses}, llevas {alcancia} ahorrados de {precio_consola}.")

print(f"En total tienes {alcancia} ahorrados en {meses}")
print("Ya tienes dinero suficiente para comprar la consola!")