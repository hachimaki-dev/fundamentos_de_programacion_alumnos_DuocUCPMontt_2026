suma_almuerzo_impresion = 0
for numeroDia in range(1, 6):
    print(f"dia {numeroDia}")
    dinero_almuerzo = int(input("cuanto dinero usaste hoy en el almuerzo?: "))
    impreciones_al_dia = int(input("cuantas impreciones hiciste hoy?"))
    total_impresiones = impreciones_al_dia * 50
    suma_almuerzo_impresion = suma_almuerzo_impresion + (dinero_almuerzo + total_impresiones)
print(suma_almuerzo_impresion)
if suma_almuerzo_impresion > 20000:
    print("alertaaa!!! presupuesto alto")
else:
    print("presupuesto moderado :)")