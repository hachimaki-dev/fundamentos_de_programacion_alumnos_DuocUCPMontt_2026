dinero_gastado = int(input("ingresa el dinero gastado diario en el almuerzo"))
impresiones = int(input("ingresa la cantidad de impresiones diarias"))

if dinero_gastado + impresiones*50 > 20000:
    print("Alerta presupusto alto")

else:
    print("presupuesto moderado")