# Estás creando un pequeño sistema para que un estudiante universitario dimensione sus gastos semanales en la fotocopiadora y colaciones.

"""
1. Solicitar al usuario cuánto dinero gasta diariamente en almuerzo (entero).
2. Solicitar al usuario cuántas impresiones realiza al día (entero), sabiendo que cada impresión vale $50 pesos.
3. Calcular el gasto total que se proyecta considerando una semana universitaria de Lunes a Viernes (5 días).
4. Si el gasto semanal total supera los $20000, mostrar un mensaje: "Alerta: Presupuesto alto". Si no, mostrar: "Presupuesto moderado".
"""

gastos_totales = 0
valor_de_la_impresion = 50

gasto_diario_almuerzo = int(input("Porfavor ingrese su gasto diario en almuerzo: "))
impresiones_diarias = int(input("Porfavor ingrese cuantas impresiones realiza al dia: "))
impresiones_diarias = impresiones_diarias * 50
gastos_totales = (impresiones_diarias + gasto_diario_almuerzo) * 5

if gastos_totales > 20000:
    print(f"Alerta: Preuspuesto Alto (${gastos_totales})")
else:
    print(f"Presupuesto Moderado! (${gastos_totales})")