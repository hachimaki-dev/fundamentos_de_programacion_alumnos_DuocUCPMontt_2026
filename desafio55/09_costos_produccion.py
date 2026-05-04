# Ejercicio 9: Costos de Producción (Emprendimiento)
# Vas a vender poleras estampadas y necesitas calcular tus ganancias mensuales.
# Datos Iniciales: Vendes cada polera a 15000. Hacer una polera te cuesta: 4000 la tela, 2500 el estampado y 500 el empaque. Vendiste 50 poleras en el mes.
# Reglas de Negocio: La ganancia por cada polera es su precio de venta menos todo lo que te costó hacerla. 
# La ganancia del mes es esa ganancia por unidad multiplicada por las poleras que vendiste.
# Restricciones: No escribas el resultado a mano, deja que Python haga las sumas y multiplicaciones. Imprime tu ganancia mensual final.

precio_polera = 15000
precio_tela = 4000
precio_estampado = 2500
precio_empaque = 500
poleras_vendidas = 50

costo_polera = precio_tela + precio_estampado + precio_empaque
ganancia_total = (precio_polera * poleras_vendidas) - (costo_polera * poleras_vendidas)
print(ganancia_total)