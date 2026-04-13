impresion = 50

gasto_diario = int(input("¿Cuanto gastas diariamente?:$ "))
impresiones =  int(input("¿Cuantas impresiones realizas cada dia?: "))

gasto_semanal = gasto_diario * 5
gasto_semanal_impresiones = (impresiones * impresion) * 5
total_semanal = gasto_semanal + gasto_semanal_impresiones

print(f"El total de gastos semanal es de ${total_semanal}")

if total_semanal > 20000:
    print("Alerta: Presupuesto alto")

else:
    print("Su presupuesto es moderado")