almuerzo = int(input("¿Cuánto gastas en promedio en tu almuerzo por día? $"))
impresiones = int(input("\n¿Cuántas impresiones realizas en promedio por día? "))

total = ((impresiones *50) + almuerzo) * 5
    
if total >= 20000:
    print(f"Alerta: Presupuesto alto.\nHas gastado ${total}")

else:
    print(f"Presupuesto moderado.\nHas gastado ${total}")
    
