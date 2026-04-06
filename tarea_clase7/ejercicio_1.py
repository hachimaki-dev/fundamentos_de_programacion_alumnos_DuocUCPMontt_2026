valor_impresion = 50
gasto_comida = 0
total_gastado = 0

comida = int(input("Cuanto dinero gastas diariamente en almuerzo?: "))
gasto_comida += comida
impresion = int(input("Cuantas impresiones realizaste?: "))
valor_impresion *= impresion

print(f"El dinero gastado en impresiones esta semana es de ${valor_impresion}")

total_gastado = (valor_impresion + gasto_comida)

print(f"El dinero gastado en comida es de ${gasto_comida}")
print(f"El total de dinero gastado esta semana es de ${total_gastado * 5}")

if total_gastado > 20000:
    print("Alerta, Presupuesto Alto!")

else:
    print("Presupuesto moderado.")