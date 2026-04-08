gasto_maximo = 20000
valor_impresión = 50
impresiones_diarias = 0
gasto_almuerzo_usuario = 0
gasto_semanal = 0

print("CALCULADOR DE GASTOS SEMANALES PARA UNIVERSITARIOS")
gasto_almuerzo_usuario = int(input("¿Cuanto gasta a diario en almuerzo?"))
impresiones_diarias = int(input("¿Cuántas impresiones al día hace?"))
impresiones_diarias = impresiones_diarias * valor_impresión
gasto_semanal = gasto_almuerzo_usuario + impresiones_diarias
if gasto_semanal > gasto_maximo:
    print(f"el dinero total que se gasta en la semana es {gasto_semanal} pesos y sobrepasa el gasto semanal de {gasto_maximo} Piensa en administrar mejor tus gastos")
else:
    print(f"El dinero que se gasta en la semana es {gasto_semanal} pesos")