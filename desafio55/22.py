alcancia = 0
ahorro_x_mes = 80000
precio_consola = 450000
meses = 0
while alcancia != precio_consola:
    alcancia += ahorro_x_mes
    meses += 1
    if alcancia >= precio_consola:
        break
print(meses)