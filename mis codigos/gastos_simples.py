almuerzo = int(input("Ingrese el monto diario en almuerzo: "))
impresiones = int(input("Ingrese la cantidad de impresiones al dia: "))
impresion = 50;
if almuerzo + impresiones * impresion > 20000:
    print("Alerta: Presupuesto alto")
else:
    print("Presupuesto moderado")
