almuerzo = int(input("¿Cuanto dinero gastas diariamente en el almuerzo?"))
impresiones = int(input("¿cuántas impresiones realiza al día?")) 
gasto_semanal = (almuerzo * 5) + (impresiones * 5 * 50)

print(f"Su gasto semanal es en total es de {gasto_semanal} pesos")

if gasto_semanal > 20000:
    print("Alerta: Presupuesto alto")
else:
    print("Pesupuesto moderado")
print("Fin")






