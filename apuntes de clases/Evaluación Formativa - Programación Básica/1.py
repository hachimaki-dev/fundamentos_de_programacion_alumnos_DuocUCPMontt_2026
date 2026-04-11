colacion_diaria = int(input("¿Cuanto dinero gasta diarimente en almuerzos?: "))
impresiones_al_dia = int(input("¿Cuantas impresiones realiza al dia(tomando en cuenta que cada impresion cuesta $50 pesos): "))
    
total_diario = impresiones_al_dia * 50 + colacion_diaria
gasto_total_semanal = total_diario * 5

if gasto_total_semanal > 20000 :
    print(f"Alerta: Presupuesto alto , usted a gastado {gasto_total_semanal} en la semana")
else:
    print(f"Presupuesto moderado , usted a gastado en la semana {gasto_total_semanal}")

