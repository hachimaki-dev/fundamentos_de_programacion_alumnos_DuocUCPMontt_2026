#ENTRADA DE GASTOS
print("*****GASTOS SIMPLES*****")
almuerzo = int(input("ingresa tu gasto de almuerzo por día: "))
impresiones = int(input("cuántas impresiones haces al día?: "))

#GASTOS IMPRESIONES
copias = impresiones * 50

#SUMA DEL GASTO DIARIO
 
diario_total =  almuerzo + impresiones

#CÁLCULO SEMANAL (LUNES A VIERNES)
total_final = diario_total * 5

#MOSTRAR RESULTADO
print("tu gasto semanal es:", total_final)

#CONDICIÓN
if total_final > 20000:
    print("Alerta presupuesto alto") 
else:
    print("Presupuesto moderado")
    

