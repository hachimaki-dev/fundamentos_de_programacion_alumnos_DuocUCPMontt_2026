"""  Estás creando un pequeño sistema para que un estudiante universitario
 dimensione sus gastos semanales en la fotocopiadora y colaciones.


Requerimientos:
1. Solicitar al usuario cuánto dinero gasta diariamente en almuerzo (entero).
2. Solicitar al usuario cuántas impresiones realiza al día (entero), sabiendo
 que cada impresión vale $50 pesos.

3. Calcular el gasto total que se proyecta considerando una semana universitaria
 de Lunes a Viernes (5 días).

4. Si el gasto semanal total supera los $20000, mostrar un mensaje:
 "Alerta: Presupuesto alto". Si no, mostrar: "Presupuesto moderado"."""

dia = 0
impreciones = 150 
while dia < 5:
    dinero = int(input("cuando dinero gastas?: "))
    impreciones_diarias = int(input("cuantas impreciones diarias haces ?"))
    
    impreciones = impreciones_diarias * impreciones
    dinero = dinero + dinero 
    dinero_semanal = dinero + impreciones 
    dia = dia + 1
    
if dinero_semanal > 20000:
    print("presupuesto alto")
else:
    print("presuouesto moderado")

