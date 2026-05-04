#Vas a vender poleras estampadas y necesitas calcular tus ganancias mensuales.

#Datos Iniciales: Vendes cada polera a 15000. Hacer una polera te cuesta: 4000 la tela, 2500 el estampado y 500 el empaque. Vendiste 50 poleras en el mes.

#Reglas de Negocio: La ganancia por cada polera es su precio de venta menos todo lo que te costó hacerla. La ganancia del mes es esa ganancia por unidad multiplicada por las poleras que vendiste.

#Restricciones: No escribas el resultado a mano, deja que Python haga las sumas y multiplicaciones. Imprime tu ganancia mensual final.
venta_polera = 15000
hacer_poleras = 4000 + 2500 + 500
la_ganancia = venta_polera - hacer_poleras 
ganancia_del_mes = la_ganancia * 50 
print(ganancia_del_mes)

