almuerzo_por_dia = int(input("¿Cuánto gastas diariamente en almuerzo? "))

costo_semanal_almuerzo = almuerzo_por_dia * 5



valor_de_cada_impresion = 50

impresiones_por_dia = int(input("¿Cuántas fotocopias sacas al día? "))

costo_impresiones = impresiones_por_dia * valor_de_cada_impresion

costo_semanal_impresiones = costo_impresiones * 5






costo_semanal_total = costo_semanal_almuerzo + costo_semanal_impresiones

if costo_semanal_total > 20000:
    print("Alerta: Presupuesto alto")
elif costo_semanal_total < 20000:
    print("Presupuesto moderado")