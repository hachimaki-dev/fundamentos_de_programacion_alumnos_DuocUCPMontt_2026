impre = 50
almuerzo = 0
dia = 1

dias = 5
gasto_semanal = 0
while dia <= dias :

    print(f"dia {dia}")
    almuerzo = int(input("Cuanto dinero gastaste en el almuerzo:"))
   
    gasto_semanal = gasto_semanal + almuerzo 
    
    impresion = int(input("Cuanto gastaste en las impresiones"))
   
    valor_impresiones = impresion*impre
    gasto_semanal = gasto_semanal + valor_impresiones 
    
    
    

    

    print(f"vas en el dia {dia}")


   
   
   
    dia = dia + 1
    
    
     




if gasto_semanal > 20000 :
    print("Alerta, presupuesto alto ")


else :
    print("presupuesto moderado")

print("Final de programa")
print(f"tu total de gasto semanal es {gasto_semanal}")