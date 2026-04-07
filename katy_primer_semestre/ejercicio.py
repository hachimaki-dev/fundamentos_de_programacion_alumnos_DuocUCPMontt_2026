# solicitar datos al usuario
gasto_diario =int(input("¿cuanto gastas diariamente en almuerzo? "))

impresiones_diarias = int(input("¿cuantas impresiones haces diariamente?"))

#impresiones cuestan $50 
costo_impresiones = impresiones_diarias * 50

#gasto total diario
gasto_diario_total = gasto_diario + costo_impresiones

# semana universitaria (5 dias)
gasto_semanal = gasto_diario_total * 5

print("tu gasto semanal es de:", gasto_semanal) 

if gasto_semanal > 1000:
   print("tu gasto semanal es alto, considera reducir tus gastos en almuerzo o impresiones")
else:
    print("tu gasto semanal es bueno, sigue así!!")
