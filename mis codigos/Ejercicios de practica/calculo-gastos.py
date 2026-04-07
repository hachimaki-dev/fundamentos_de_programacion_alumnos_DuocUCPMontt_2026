#dinero_almuerzo = 0
#dinero_impresiones = 0
gasto_total = 0
dia_semana = 0


print("~~~ BIENVENIDO A LA CALCULADORA DE GASTOS ~~~")

while dia_semana < 5:

    dinero_almuerzo = int(input("¿Cuanto dinero haz gastado hoy Lunes en el almuerzo?"))
    numero_impresiones = int(input("¿Cuantas impresiones realizo hoy Lunes?"))
    
    numero_impresiones *= 50
    print(f"dinero gastado en impresiones: {numero_impresiones}")
    gasto_total = gasto_total + dinero_almuerzo + numero_impresiones
    dia_semana += 1

    dinero_almuerzo = int(input("¿Cuanto dinero haz gastado hoy martes en el almuerzo?"))
    numero_impresiones = int(input("¿Cuantas impresiones realizo hoy martes?"))
    
    numero_impresiones *= 50
    print(f"dinero gastado en impresiones: {numero_impresiones}")
    gasto_total = gasto_total + dinero_almuerzo + numero_impresiones
    dia_semana += 1

    dinero_almuerzo = int(input("¿Cuanto dinero haz gastado hoy miercoles en el almuerzo?"))
    numero_impresiones = int(input("¿Cuantas impresiones realizo hoy miercoles?"))
    
    numero_impresiones *= 50
    print(f"dinero gastado en impresiones: {numero_impresiones}")
    gasto_total = gasto_total + dinero_almuerzo + numero_impresiones
    dia_semana += 1

    dinero_almuerzo = int(input("¿Cuanto dinero haz gastado hoy jueves en el almuerzo?"))
    numero_impresiones = int(input("¿Cuantas impresiones realizo hoy jueves?"))
    
    numero_impresiones *= 50
    print(f"dinero gastado en impresiones: {numero_impresiones}")
    gasto_total = gasto_total + dinero_almuerzo + numero_impresiones
    dia_semana += 1

    dinero_almuerzo = int(input("¿Cuanto dinero haz gastado hoy viernes en el almuerzo?"))
    numero_impresiones = int(input("¿Cuantas impresiones realizo hoy viernes?"))
    
    numero_impresiones *= 50
    print(f"dinero gastado en impresiones: {numero_impresiones}")
    gasto_total = gasto_total + dinero_almuerzo + numero_impresiones
    dia_semana += 1   


if gasto_total > 20000:
    print("Alerta: Presupuesto alto")

else:
    print("Presupuesto moderado")



