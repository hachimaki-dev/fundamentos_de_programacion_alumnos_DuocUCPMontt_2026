# 1. El Cálculo de Gastos Simples
# Estás creando un pequeño sistema para que un estudiante universitario dimensione sus gastos semanales en la fotocopiadora y colaciones.

# Requerimientos:
# 1. Solicitar al usuario cuánto dinero gasta diariamente en almuerzo (entero).
# 2. Solicitar al usuario cuántas impresiones realiza al día (entero), sabiendo que cada impresión vale $50 pesos.
# 3. Calcular el gasto total que se proyecta considerando una semana universitaria de Lunes a Viernes (5 días).
# 4. Si el gasto semanal total supera los $20000, mostrar un mensaje: "Alerta: Presupuesto alto". Si no, mostrar: "Presupuesto moderado".

print("****El Cálculo de Gastos Simples****")

gastos_almuerzo = int(input("¿Cuánto dinero gasta diariamente en almuerzo?: "))
impresiones_dia = int(input("¿Cuántas impresiones haces al día?: "))

total_impresiones_dia = impresiones_dia * 50
total_impresiones = total_impresiones_dia * 5
gasto_total = gastos_almuerzo * 5

if total_impresiones + gasto_total > 20000:
    print("Alerta: Presupuesto alto")
else:
    print("Presupuesto moderado")

print("Fin del programa :D")

