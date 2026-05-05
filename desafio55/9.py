poleras = 15000
#productos de las poleras
telas = 4000
estanpado = 2500
empaque = 500
poleras_vendidas = 50

ganacias = poleras - telas - estanpado - empaque
ganancia_mensual = ganacias * poleras_vendidas
print("tus ganacias mensueles fueron", ganancia_mensual)