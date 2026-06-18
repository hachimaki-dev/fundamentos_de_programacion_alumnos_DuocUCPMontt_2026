print("=== Calculadora de Gastos Simples ===")

almuerzo = int(input("¿Cuanto gastas diariamente en tu almuerzo?: "))
impresiones = int(input("¿Cuanto gastas en imprsiones a diario?: "))

gasto_impresiones = impresiones * 50
gasto_diario = almuerzo + gasto_impresiones
gasto_semanal = gasto_diario * 5

print("El gasto semanal proyectado es:", gasto_semanal)

if gasto_semanal > 20000 :
    print("Alerta: presupuesto alto")
else:
    print("Presupuesto estable")