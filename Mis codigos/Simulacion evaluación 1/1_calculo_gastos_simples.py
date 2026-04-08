# 1. El Cálculo de Gastos Simples
# Estás creando un pequeño sistema para que un estudiante universitario dimensione sus gastos semanales en la fotocopiadora y colaciones.

# Requerimientos:
# 1. Solicitar al usuario cuánto dinero gasta diariamente en almuerzo (entero).
# 2. Solicitar al usuario cuántas impresiones realiza al día (entero), sabiendo que cada impresión vale $50 pesos.
# 3. Calcular el gasto total que se proyecta considerando una semana universitaria de Lunes a Viernes (5 días).
# 4. Si el gasto semanal total supera los $20000, mostrar un mensaje: "Alerta: Presupuesto alto". Si no, mostrar: "Presupuesto moderado".

# Desglose de Lógica:
# Necesitas un input convertido a int para dinero, y otro para impresiones. 
# Multiplica impresiones por 50 y suma el gasto de colación. Todo eso multiplícalo por 5. Guarda en variable, y aplica el condicional simple.

print(" GASTOS SIMPLES ".center(30, "-"))

# SIN FOR
# dinero_almuerzo = int(input("Gasto diario en almuerzo: "))
# cantidad_impresiones = int(input("Cantidad diaria de impresiones: "))
# gasto_semanal = dinero_almuerzo*5 + (cantidad_impresiones*50)*5

# print("------------------------------------")
# print(f"Gasto semanal presupuestado: ${gasto_semanal}")

# if gasto_semanal > 20000:
#     print("Alerta: Presupuesto Alto")
# else:
#     print("Presupuesto moderado")


# CON FOR
dinero_almuerzo = 0
cantidad_impresiones = 0
gasto_semanal = 0

for dia_semana in range (1,6):
    dinero_almuerzo = int(input(f"Gasto almuerzo dia {dia_semana}: "))
    cantidad_impresiones = int(input(f"Cantidad impresiones dia {dia_semana}: "))
    gasto_semanal = gasto_semanal + dinero_almuerzo + (cantidad_impresiones * 50)

print("------------------------------------")
print(f"Gasto semanal presupuestado: ${gasto_semanal}")

if gasto_semanal > 20000:
    print("Alerta: Presupuesto Alto")
else:
    print("Presupuesto moderado")