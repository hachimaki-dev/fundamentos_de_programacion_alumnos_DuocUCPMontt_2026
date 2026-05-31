rangos_de_ventas = {"Venta mayor" : 0, "Venta media" : 0, "Venta menor": 0}
contador = 1
while contador < 7:
    try:
        valor_de_la_venta = int(input(f"¿Cuanto fue el precio por el que se vendió el producto n°{contador}?\n"))
        if valor_de_la_venta < 0:
            print("Debe ingresar solo enteros positivos.")
            continue
        if valor_de_la_venta > 50000:
            print("Venta mayor.")
            rangos_de_ventas["Venta mayor"] += 1
            contador+=1
        elif valor_de_la_venta >= 10000 and valor_de_la_venta <= 50000:
            print("Venta media.")
            rangos_de_ventas["Venta media"] += 1
            contador+=1
        else:
            print("Venta menor")
            rangos_de_ventas["Venta menor"] += 1
            contador+=1
    except ValueError:
        print("Debe ingresar entero positivo para poner el valor del producto que fue vendido.")
print(rangos_de_ventas)