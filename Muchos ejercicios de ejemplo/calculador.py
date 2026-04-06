print("bienvenido")

impre = 50
almuerzo = 0
caja = 0
dia = 1
dias = 6
while dia != dias :
    almuerzo = int(input("cuanto dinero gastaste en almuerzo"))
    caja = caja + almuerzo
    impresion = int(input("cuantas impresiones has hecho hoy"))
    subtotal = impresion*impre
    caja = caja + subtotal
    print(f"estas en el dia {dia}")
    dia = dia + 1

if caja > 20000 :
    print("alerta presupuesto alto")
elif caja < 20000 :
    print("presupuesto moderado")

print("fin")
print(f"has gastado en total{caja}")
