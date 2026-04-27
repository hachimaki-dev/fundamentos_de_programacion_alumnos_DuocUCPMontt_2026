# TERMINADO

print("====== GASTOS SIMPLES ======")


impresiones = 50

ALMUERZO_GASTOS = int(input("¿Cuánto gastas en el almuerzo?: $"))
IMPRESIONES_GASTOS = impresiones * int(input("¿Cuántas impresiones haces?: "))

GASTO_SEMANA_TOTAL = ALMUERZO_GASTOS + IMPRESIONES_GASTOS * 5

if GASTO_SEMANA_TOTAL > 20000:
    print(f"¡ALERTA! presupuesto alto")
elif GASTO_SEMANA_TOTAL < 20000:
    print(f"Presupuesto moderado")
    
