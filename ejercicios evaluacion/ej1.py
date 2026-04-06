print ("Bienvenido a su calculadora de gastos")

impresiones = 50 

comida = int(input("ingrese cuanto gasta diaramente en colacion "))
cant_impresiones = int(input("Ingrese cuantas impresiones realiza al dia "))

total_impresiones = impresiones * cant_impresiones

comida_semanal = comida * 5

impresiones_semanal = total_impresiones * 5

total = (comida_semanal + impresiones_semanal)

if total > 20000:
    print ("Excede presupuesto")
else:
    print ("Dentro del presupuesto")