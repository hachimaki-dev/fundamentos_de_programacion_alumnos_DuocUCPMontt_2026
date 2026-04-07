#El Cálculo de Gastos Simples

almuerzos = int(input("cuanto dinero gasta diaramente en almuerzos "))
impresiones = int(input("cuantas impresiones realizas al dia "))
total = ((almuerzos + impresiones * 50)*5)
if total > 20000:
 print ("Alerta: Presupuesto alto")
else:
 print ("Presupuesto moderado")
print (total )