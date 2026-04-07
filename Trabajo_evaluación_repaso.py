almuerzo = int(input("Ingrese su dinero gastado diariamente:"))
impresiones = int(input("Cuántas impresiones realiza por día:"))

Valor_De_Impresion = impresiones * 50
Valor_De_Almuerzo = almuerzo * 5

if Valor_De_Almuerzo + Valor_De_Impresion > 20000:
    print("Alerta: Presupuesto alto")
else :
    print("Presupuesto moderado")   