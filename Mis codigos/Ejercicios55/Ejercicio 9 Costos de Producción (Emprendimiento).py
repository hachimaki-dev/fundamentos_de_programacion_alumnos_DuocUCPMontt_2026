# Ejercicio 9: Costos de Producción (Emprendimiento)
# Vas a vender poleras estampadas y necesitas calcular tus ganancias mensuales.

# Datos Iniciales: Vendes cada polera a 15000. Hacer una polera te cuesta: 4000 la tela, 2500 el estampado y 500 el empaque. Vendiste 50 poleras en el mes.

# Reglas de Negocio: La ganancia por cada polera es su precio de venta menos todo lo que te costó hacerla. La ganancia del mes es esa ganancia por unidad multiplicada por las poleras que vendiste.

# Restricciones: No escribas el resultado a mano, deja que Python haga las sumas y multiplicaciones. Imprime tu ganancia mensual final.

POLERA = 15000

#COSTOS
TELA = 4000
ESTAMPADO = 2500
EMPAQUE = 500

ventas_en_el_mes = 50

ganancias_unidad = POLERA - TELA - ESTAMPADO - EMPAQUE

ganancias_totales = ganancias_unidad * ventas_en_el_mes

print(ganancias_totales)

