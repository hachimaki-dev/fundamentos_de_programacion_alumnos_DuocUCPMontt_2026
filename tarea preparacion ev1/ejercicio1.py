almuerzo = int(input("cuanto gasta en almuerzo?"))
fotocopia = int(input("cuanto gasta en fotocopia?"))


gasto_fotocopia = fotocopia * 50
gasto_diario = almuerzo + gasto_fotocopia 

gasto_semanal= gasto_diario * 5

print("gasto semanal es:", gasto_semanal)


if gasto_semanal > 20000:
   print("alerta presupuesto alto")
else:
   print("presupuesto moderado")

print("listo")
   