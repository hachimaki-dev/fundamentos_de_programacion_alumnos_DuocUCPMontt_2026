dinero_almuerzo= int(input("Ingrese dinero utilizado a diario en almuerzo: "))
print("PRECIO X FOTOCOPIA ES 50 PESOS")
N_fotocopia= int(input("Ingrese cantidad de impresiones al dia: "))
N_fotocopia= N_fotocopia * 50
gasto_semanal= dinero_almuerzo + N_fotocopia
gasto_semanal= gasto_semanal * 5
print(f"tu gasto es de {gasto_semanal}")
if gasto_semanal > 20000:
    print("ALERTA, PRESUPUESTO ALTO")
else:
    print("PRESUPUESTO MODERADO")