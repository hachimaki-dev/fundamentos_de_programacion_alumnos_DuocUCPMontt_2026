'''
1. Solicitar al usuario cuánto dinero gasta diariamente en almuerzo (entero).
2. Solicitar al usuario cuántas impresiones realiza al día (entero), sabiendo que cada impresión vale $50 pesos.
3. Calcular el gasto total que se proyecta considerando una semana universitaria de Lunes a Viernes (5 días).
4. Si el gasto semanal total supera los $20000, mostrar un mensaje: "Alerta: Presupuesto alto". Si no, mostrar: "Presupuesto moderado".
'''

NUMERO_DIAS = 5
PRECIO_IMPRESION = 50

gasto_diario = int (input("¿Cuánto dinero gasta diariamente?\n"))
num_impresiones = int (input("Cuántas impresiones realiza al día?\n"))

gasto_total_semana = ((gasto_diario * NUMERO_DIAS) + num_impresiones * PRECIO_IMPRESION * NUMERO_DIAS)

if gasto_total_semana > 20000 :
    print(f"Alerta: Presupuesto alto ({gasto_total_semana}).")
else :
    print(f"Presupuesto moderado ({gasto_total_semana})")