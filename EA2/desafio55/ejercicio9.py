'''Ejercicio 9: Costos de Producción (Emprendimiento)
Vas a vender poleras estampadas y necesitas calcular tus ganancias mensuales.

Datos Iniciales: Vendes cada polera a 15000. Hacer una polera te cuesta: 4000 la tela, 2500 el estampado y 500 el empaque. Vendiste 50 poleras en el mes.

Reglas de Negocio: La ganancia por cada polera es su precio de venta menos todo lo que te costó hacerla. La ganancia del mes es esa ganancia por unidad multiplicada por las poleras que vendiste.

Restricciones: No escribas el resultado a mano, deja que Python haga las sumas y multiplicaciones. Imprime tu ganancia mensual final.'''

precio_polera = 15000
tela = 4000
estampado = 2500
empaque = 500
costos = tela + estampado + empaque
ganancia = precio_polera - costos 
ventas = 50
ganancia_mensual = ganancia * ventas
print(f"Ganancia final: {ganancia_mensual}")

