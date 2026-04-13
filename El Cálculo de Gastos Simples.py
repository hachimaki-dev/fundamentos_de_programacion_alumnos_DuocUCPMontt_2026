
dinero_almuerzo = int(input("¿Cuanto Dinero gastas diariamente en almuerzo?: $ "))
impresiones_diarias  = int(input(f"¿Cuantas impresiones haces diariamente?: "))

valor_impresion = 50

gasto_diario = dinero_almuerzo + (impresiones_diarias * valor_impresion)
gasto_semanal = gasto_diario * 5 #igual podria ser gasto_semanal = 5 * (dinero_almuerzo + (impresiones_diarias * 50))

print(f"El gasto total proyectado para la semana es: ${gasto_semanal}")

if gasto_semanal > 20000 :
    print("Alerta: Presupuesto Alto")
else:
    print("Presupuesto Moderado")







