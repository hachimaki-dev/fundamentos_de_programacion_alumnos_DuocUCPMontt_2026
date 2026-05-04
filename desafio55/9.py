#Vas a vender poleras estampadas y necesitas calcular tus ganancias mensuales.
#Datos Iniciales: Vendes cada polera a 15000. Hacer una polera te cuesta: 4000 la tela, 2500 el estampado y 500 el empaque. Vendiste 50 poleras en el mes.
#Reglas de Negocio: La ganancia por cada polera es su precio de venta menos todo lo que te costó hacerla. 
#La ganancia del mes es esa ganancia por unidad multiplicada por las poleras que vendiste.
#Restricciones: No escribas el resultado a mano, deja que Python haga las sumas y multiplicaciones. Imprime tu ganancia mensual final.400000
valor_por_polera = 15000
tela = 4000
estampado = 2500
empaque = 500
poleras_vendidas = 50
mano_de_obra = tela + estampado + empaque
ganacia_por_polera = valor_por_polera - mano_de_obra
ganancia_del_mes = ganacia_por_polera * poleras_vendidas
print(ganancia_del_mes)
