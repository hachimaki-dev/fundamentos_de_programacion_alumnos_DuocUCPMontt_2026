print("bienvenido/a a la boleteria")
total_recaudado = 0
nombre_destino_3 = "Osorno"
nombre_destino_2 = "Frutillar"
nombre_destino_1 = "Puerto Varas"

precio_destino_3 = 7000
precio_destino_2 = 5000
precio_destino_1 = 3000

print("        -        elija su destino")
print("        -        1- Puerto Varas $3.000")
print("        -        2- Frutillar $5.000")
print("        -        3- Osorno $7.000")

opcion_destino = int(input("por favor ingrese su destino: "))


if opcion_destino == 1 :
print(g"ha elegido Puerto Varas el costo es de \n 1. Pasaje de ida ${precio_destino_1} \n 2. Pasaje de ida y vuelta ${precio_destino_1 * 2}")

tipo_viaje = int(input("va de ida? o de ida y vuelta?"))

print(f"ha eleido de ida el costo es de ${precio_destino_1 * 2}")
      
      
      
if tipo_viaje == 1 :
    total_recaudado =total_recaudado + precio_destino_1
elif tipo_viaje == 2 :
    total_recaudado =total_recaudado + (precio_destino_1 * 2)   