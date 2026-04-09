"""
Estás creando un pequeño sistema para que un estudiante universitario dimensione sus gastos semanales en la fotocopiadora y colaciones.

Requerimientos:
1. Solicitar al usuario cuánto dinero gasta diariamente en almuerzo (entero).
2. Solicitar al usuario cuántas impresiones realiza al día (entero), sabiendo que cada impresión vale $50 pesos.
3. Calcular el gasto total que se proyecta considerando una semana universitaria de Lunes a Viernes (5 días).
4. Si el gasto semanal total supera los $20000, mostrar un mensaje: "Alerta: Presupuesto alto". Si no, mostrar: "Presupuesto moderado".
"""

Almuerzo = int(input("Cuanto dinero gastas en tu almuerzo a diario?"))
Impresiones = int(input("Cuantas impresiones realizas al dia?"))
Total = Almuerzo * 5 + Impresiones * 250
print(f"Gastas ${Total} de lunes a viernes")
if Total > 20000:
    print("Alerta: Presupuesto alto")
else:   
    print("Presupuesto moderado")