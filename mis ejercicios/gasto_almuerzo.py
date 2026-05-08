almuerzo = int(input("gastos de almuerzo"))
impresiones =int(input("gastos de impresiones"))

total= (almuerzo + (impresiones * 50)) * 5

print(f"total semanal: ${total}")

if total > 20000:
    print("alerta presupuesto alto")
else :
    print("presupuesto moderado")
    
    #geminis 