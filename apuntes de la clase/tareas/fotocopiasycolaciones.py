colacion = 500
fotocopias = 50
gasto_total_colaciones = 0
gastos_totales_impreciones = 0
gasto_total = 0

print("hola bienvenidos a esta app para ayudarte a calcular tus gastos semanales")
print(" la colacion vale 500 pesos")
print("las fotocopias valen 50 pesos cada una")
colacion = int(input("¿cuantas colaciones compras al dia? "))
fotocopias = int(input("¿cuantas impreciones haces al dia? "))

gasto_total_colaciones = (colacion*500) *5
gastos_totales_impreciones = (fotocopias*50) *5
gasto_total = gastos_totales_impreciones + gasto_total_colaciones
print(f"tus gastos semanales de colaciones es de {gasto_total_colaciones} y tus gastos de fotocopias son {gastos_totales_impreciones}")

print(f"el gasto total mensual es de {gasto_total}")

if gasto_total > 20000:
    print("¡Presupuesto alto!")
if gasto_total < 2000:
    print("presupuesto moderado")