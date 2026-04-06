dia = 0
while dia >= 5 :
    dia = dia + 1
    almuerzo_diario = int(input("Porfavor ingresar gasto diario en almuerzo: "))
    impresiones = 50 
    impresiones_diarias = int(input("Ingresar cuantas impresiones realiza diario: "))
    Valor_de_todas_las_impresiones= int(print(f"{impresiones * impresiones_diarias}"))
    Gastos = int(print(f"{almuerzo_diario + Valor_de_todas_las_impresiones}"))
    if Gastos > 20000:
        print("Presupuesto elevado, por favor abaratar costos")
    elif Gastos < 20000:
        print("Presupuesto Moderado")
    
    

