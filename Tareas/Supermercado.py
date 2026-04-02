producto_estrella = 10000
productos_a_llevar = 0
bandera = True
import time

print("Bienvenido al Supermercado de Python, y para su fortuna tenemos nuestro PRODUCTO ESTRELLAAAA")
time.sleep (4)
print("Al llevar 5 o más productos tendras un majestuoso 10% DE DESCUENTOOOO")
time.sleep (2)
print("Pero por esta unica vez si llevas 10 productos o más te llevas un 20% DE DESCUENTOOOOO")
time.sleep (2)

while bandera:
    productos_a_llevar = int(input("Cuantos productos estrella desea llevar")
    confirmacion = input(f"Estas seguro que quieres llevar {productos_a_llevar} productos (Responder con "SI" o con "NO")
    