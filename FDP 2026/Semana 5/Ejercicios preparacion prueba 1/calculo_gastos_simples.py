gasto_semanal_total = 0

for i in range(5):
    gasto_diario_almuerzo = int(input("Ingrese su gasto diario en almuerzo: $"))

    cant_impresiones = int(input("Ingresa cuantas impresiones haces al día: "))

    gasto_semanal_total += gasto_diario_almuerzo + (50 * cant_impresiones)

if gasto_semanal_total > 20000:
    print("Alerta: presupuesto alto")
else:
    print("Presupuesto moderado")