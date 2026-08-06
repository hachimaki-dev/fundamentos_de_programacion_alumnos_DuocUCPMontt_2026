""" Ejercicio 15 — Sistema de control de inventario de una tienda
Una tienda de electrónica comienza con 80 unidades de un producto en stock.
 Capacidad máxima de la bodega: 200 unidades. El encargado usa el siguiente menú:

=== INVENTARIO TIENDA DIGITAL ===
1. Ver stock actual
2. Registrar entrada de mercancía
3. Registrar venta
4. Salir
Validaciones:

La entrada debe ser un entero positivo

El stock resultante no puede superar la capacidad máxima 
(es decir: stock + entrada <= 200). 
No basta con validar que la entrada sea menor que 200.

La venta no puede superar el stock actual
Ambos valores deben ser enteros positivos

Ejemplo: Si el stock actual es 180 y el usuario intenta ingresar 30 unidades, 
debe rechazarse porque 180 + 30 = 210 > 200, aunque 30 < 200.

Al salir: "Stock final: {stock} unidades. Sesión cerrada." """

stock_de_inicio = 80 

bodega = 80

while True:
    try:
        menu = int(input("=== INVENTARIO TIENDA DIGITAL ===\n 1. Ver stock actual\n 2. Registrar entrada de mercancía\n 3. Registrar venta \n 4. Salir"))

        if menu == 1:
            print(f"el stock actual es : {bodega}")
        
        elif menu == 2:
            stock_de_entrada = int(input("ingresa la cantidad del stock entrante : "))
            if stock_de_entrada > 0:
                if stock_de_entrada + stock_de_inicio <= 200:
                    bodega = stock_de_inicio + stock_de_entrada
                elif stock_de_entrada + stock_de_inicio > 200:
                    print("El stock resultante no puede superar la capacidad máxima")
            else:
                print("ingresa un numero de stock mayor a 0")
        
        elif menu == 3:
            ventas = int(input("registra la venta de stock : "))
            if ventas < 0 :
                print("las ventas no pueden ser menor que 0")
            elif ventas > bodega:
                print("las ventas no pueden ser mayor que el stock existente")
            else:
                bodega -= ventas
        
        elif menu == 4:
            break

        else:
            print("ingresa una de las opciones validas del 1 al 4")

    except ValueError:
        print("ingresa un numero entero y valido")

print(f"Stock final: {bodega} unidades. Sesión cerrada.")