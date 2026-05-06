alcancia= 0
ahorro_x_mes= 80000
valor_consola= 450000
meses= 0

while alcancia <= valor_consola:
    alcancia= alcancia + ahorro_x_mes
    meses += 1

print(f"Lo lograste, juntaste lo que necesitabas en {meses} meses")