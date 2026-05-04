"""Ejercicio 9: Costos de Producción (Emprendimiento)
Vas a vender poleras estampadas y necesitas calcular tus ganancias mensuales.

Datos Iniciales: Vendes cada polera a 15000. Hacer una polera te cuesta: 4000 la tela, 2500 el estampado y 500 el empaque. Vendiste 50 poleras en el mes.

Reglas de Negocio: La ganancia por cada polera es su precio de venta menos todo lo que te costó hacerla. 

La ganancia del mes es esa ganancia por unidad multiplicada por las poleras que vendiste.

Restricciones: No escribas el resultado a mano, deja que Python haga las sumas y multiplicaciones. Imprime tu ganancia mensual final."""

Polera = 15000

Tela = 4000

Estampado = 2500

Empaque = 500

Poleras_vendidas_este_mes = 50

Gasto_crear_Polera = Tela + Estampado + Empaque

Ganancia_Total = Polera * Poleras_vendidas_este_mes - Gasto_crear_Polera * Poleras_vendidas_este_mes

print(Ganancia_Total)



