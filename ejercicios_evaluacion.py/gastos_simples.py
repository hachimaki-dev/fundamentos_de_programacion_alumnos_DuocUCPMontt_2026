suma = 0
for numeroDia in range(1, 6):
    print(f"dia {numeroDia}")
    dinero_almuerzo = int(input("dinero gastado en almuerzo hoy: "))
    impresiones = int(input("¿cuantras fotocopias realizaste hoy?"))
    total_impresion =  impresiones * 50
    suma =  suma + (dinero_almuerzo + 90000)
print(suma)
if suma >= 20000:
        print("Alerta!!! preosupuesto alto")
else:
        print("presupuesto moderado")
