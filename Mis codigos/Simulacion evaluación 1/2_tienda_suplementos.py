# 2. Tienda de Suplementos (Con Ciclos)
# Una tienda vende potes de proteína. El usuario puede agregar potes hasta que decida finalizar.

# Requerimientos:
# 1. Utiliza un ciclo (while) para preguntar repetidamente al usuario el precio de un suplemento a agregar al carrito. 
#     Si ingresa "0" u otro número de salida que definas, el ciclo debe terminar.
# 2. Lleva la cuenta del total a pagar y de la cantidad de productos ingresados.
# 3. Si el usuario compró 3 o más productos en total, aplícale un descuento del 10% al total al finalizar.
# 4. Imprime el total final a pagar y la cantidad de productos comprados.

# Desglose de Lógica:
# Declara 'total = 0' y 'contador = 0'. En tu while, mientras el precio ingresado sea > 0, agrégalo al total y suma 1 al contador. 
# Al salir del ciclo (desindentado), haz el if para el descuento (total = total * 0.9).

print(" TIENDA SUPLEMENTOS ".center(40, "-"))

total_a_pagar = 0
contador_productos = 0

while True:
    print("Ingrese 0 para pasar al pago")
    precio_suplemento = int(input("Precio del suplemento: "))
    if precio_suplemento <= 0:
        break
    else:
        total_a_pagar += precio_suplemento
        contador_productos += 1

if contador_productos >= 3:
    total_a_pagar = total_a_pagar * 0.9
    print(f"Total a pagar: ${total_a_pagar} | Cantidad de productos comprados: {contador_productos}")
else:
    print(f"Total a pagar: ${total_a_pagar} | Cantidad de productos comprados: {contador_productos}")

    
