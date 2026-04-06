#1. Solicitar al usuario cuánto dinero gasta diariamente en almuerzo (entero).
#2. Solicitar al usuario cuántas impresiones realiza al día (entero), sabiendo que cada impresión vale $50 pesos.
#3. Calcular el gasto total que se proyecta considerando una semana universitaria de Lunes a Viernes (5 días).
#. Si el gasto semanal total supera los $20000, mostrar un mensaje: "Alerta: Presupuesto alto". Si no, mostrar: "Presupuesto moderado".

gasto_diario_almuerzo = int(input("cuanto dinero gasta diariamente? "))
costo_impresion = 50
ipresiones_diarias = int(input("cuantas impresiones hace al dia? "))
costo_impresion_diaria = ipresiones_diarias * costo_impresion
semana = 5
gasto_total_semanal = (gasto_diario_almuerzo * semana) + (costo_impresion_diaria * semana)

if gasto_total_semanal > 20000:
    print("Alerta: Presupuesto alto.")
    print(gasto_total_semanal)
else:
    print("Pesupuesto moderado")
    print(gasto_total_semanal)