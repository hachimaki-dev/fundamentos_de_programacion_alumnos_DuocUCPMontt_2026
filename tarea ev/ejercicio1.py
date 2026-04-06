Almuerzo = int(input("Ingrese gastos de Almuerzo diario: "))
Impresion = int(input("Ingrese cantidad de Fotocopias diaria: "))

Total_Impresion = Impresion * 50
Total_Almuerzo = Almuerzo * 5

if Total_Almuerzo + Total_Impresion > 20000 : 
    print("Alerta:Presupuesto alto")
else :
    print("Presupuesto Moderado")