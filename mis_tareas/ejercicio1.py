colacion = int(input("gasto diario de colacion :"))
impresion = int(input("gasto diario de impresiones: "))

total_colacion = colacion * 5
total_impresion = impresion * 50
print(f"gastaste {total_impresion} en impresiones y gastaste {total_colacion} en colacion")
total = total_impresion + total_colacion
print(f"en total = {total}")
if total_colacion + total_impresion <= 20000:
    print("Presupuesto moderado")
else: 
    print("Alerta: presupuesto alto")
 