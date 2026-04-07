dias_de_la_semana = ["lunes", "martes", "miércoles", "jueves", "viernes"]
total_almuerzo = 0

print(">>>>>>>> Registro diario de gastos en comida <<<<<<<<<<")

for dia in dias_de_la_semana:
    almuerzo = int(input(f"¿Cuántos gastaste el dia {dia} en tu almuerzo? $"))
    total_almuerzo += almuerzo


impresiones = int(input("¿Cuántas impresiones realizas diariamente? "))
gasto_semanal = (total_almuerzo + (impresiones * 50)) * 5

if gasto_semanal >= 20000:
    print(f"Alerta: Presupuesto alto. Has gastado ${gasto_semanal} esta semana.")
else:
    print(f"Presupuesto moderado. Has gastado ${gasto_semanal} esta semana.")
