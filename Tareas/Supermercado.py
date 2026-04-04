producto_estrella = 10000
productos_a_llevar = 0
total_a_pagar = 0
descuento = 0
bandera = True
import time

print("Bienvenido al Supermercado de Python, y para su fortuna tenemos nuestro PRODUCTO ESTRELLAAAA")
time.sleep (4)
print("Al llevar entre 5 a 9 productos tendras un majestuoso 10% DE DESCUENTOOOO")
time.sleep (2)
print("Pero por esta unica vez si llevas 10 productos o más te llevas un 20% DE DESCUENTOOOOO")
time.sleep (2)


pregunta_precio = input("Te interesaria saber el precio (Responder con SI o NO)")
if pregunta_precio == "SI":
    print("Perfecto, el precio del producto estrella es de 10.000 CLP")
else:
    print("Vale caballero, que tenga buen dia :)")
    import sys
    sys.exit ()
while bandera:
    productos_a_llevar = int(input("Cuantos productos estrella desea llevar"))
    confirmacion = input(f"Estas seguro que quieres llevar {productos_a_llevar} productos (Responder con SI o con NO)")
    if confirmacion == "SI":
        print("Bien, podemos proseguir")
        break
    else:
        print("Entiendo, vuelve a seleccionar tu cantidad")

if productos_a_llevar <= 4:
    total_a_pagar = producto_estrella * productos_a_llevar
    print("Lastimosamente no tuvo descuento :( Que tenga buena tarde")
    print(f"Su total a pagar sería de ${total_a_pagar}CLP")
    print("QUE TENGA BUENA TARDE CHAVALIN")
if productos_a_llevar <= 9:
    total_a_pagar = producto_estrella * productos_a_llevar
    descuento = total_a_pagar * 0.1 
    total_a_pagar = total_a_pagar * 0.9
    print(f"FELICIDADES, HA TENIDO UN DESCUENTO DE {descuento}")
    print(f"Su total a pagar sería de ${total_a_pagar}CLP")
    print("QUE TENGA BUENA TARDE CHAVALINNNNN")
if productos_a_llevar >= 10:
    total_a_pagar = producto_estrella * productos_a_llevar
    descuento = total_a_pagar * 0.2 
    total_a_pagar = total_a_pagar * 0.8
    print(f"FELICIDADES, HA TENIDO UN DESCUENTO DE {descuento}")
    print(f"Su total a pagar sería de ${total_a_pagar}CLP")
    print("QUE TENGA BUENA TARDE CHAVALINNNNN") 