#Ejercicio 9: Costos de Producción (Emprendimiento)
#Vas a vender poleras estampadas y necesitas calcular tus ganancias mensuales.

#Datos Iniciales: Vendes cada polera a 15000. Hacer una polera te cuesta: 4000 la tela, 2500 el estampado y 500 el empaque. Vendiste 50 poleras en el mes.

#Reglas de Negocio: La ganancia por cada polera es su precio de venta menos todo lo que te costó hacerla. La ganancia del mes es esa ganancia por unidad multiplicada por las poleras que vendiste.

#Restricciones: No escribas el resultado a mano, deja que Python haga las sumas y multiplicaciones. Imprime tu ganancia mensual final.

"costo de producción por polera"
costo_tela = 4000
costo_estampado = 2500
costo_empaque = 500

costo_produccion_polera = costo_tela + costo_estampado + costo_empaque

50 #cantidad de poleras vendidas
polera = 15000 #precio de venta por polera 
ganancia_por_cada_polera = polera - costo_produccion_polera
ganancia_mensual = ganancia_por_cada_polera * 50
print(f"la ganancia mensual es: {ganancia_mensual}")

