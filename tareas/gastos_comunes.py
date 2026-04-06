print("----GASTOS----")
print("Si usted supera la barrera de los $20.000 pesos se mostrara en pantalla presupuesto alto")
gasto = int(input("Ingrese la cantidad diaria de cuanto gasta en almuerzo"))
impresion = int(input("Ingrese cuantas impresiones realiza diariamenrte (ingreselo como numero entero)"))
resultado_impresiones = impresion * 50
print(f"Su gasto en impresiones diaria es ${resultado_impresiones}")
resultado_comida= gasto*5
print(f"Su gasto en comida durante la semana (Lunes a Viernes) es de ${resultado_comida}")
resultado_total = resultado_impresiones + resultado_comida
print(f"Lo que usted gasta en la semana es : ${resultado_total}")
if resultado_total >= 20000: 
    print ("Alerta : presupuesto alto")
else : 
    print("Presupuesto moderado")    