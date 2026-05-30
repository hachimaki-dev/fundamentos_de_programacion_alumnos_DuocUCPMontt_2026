venta_mayor = 0
venta_media = 0
venta_menor = 0
total_recaudado = 0
ventas_dia = 0


while True:
    try:
        ventas_del_dia = int(input("Ingrese el monto de venta del dia :  "))
        ventas_dia += 1
    except ValueError :
        print("Ingrese una opcion valida ")
        continue

    
    if ventas_del_dia > 50000:
        print("Venta Mayor")
        venta_mayor += ventas_del_dia
        total_recaudado += ventas_del_dia
    elif ventas_del_dia >=  10000 and ventas_del_dia <= 50000:
        print("Venta Media")
        venta_media += ventas_del_dia
        total_recaudado += ventas_del_dia
    elif ventas_del_dia < 10000 :
        print("Venta Menor")
        venta_menor += ventas_del_dia
        total_recaudado += ventas_del_dia


    if ventas_dia == 6:
        print(f"Ventas Mayores :  {venta_mayor}")
        print(f"Ventas Medias :  {venta_media}")
        print(f"Ventas Menores :  {venta_menor}")
        print(f"Total Recaudado :  {total_recaudado}")
        break

