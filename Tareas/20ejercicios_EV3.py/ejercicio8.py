venta_Mayor = 0
venta_Media = 0
venta_Menor = 0
total = 0

for v in range(6):
    ventas = int(input(f'Ingresa la cantidad de venta {v + 1}: '))
    total += ventas

    if ventas > 50000:
        print('Venta mayor')
        venta_Mayor += 1
    elif ventas >= 10000:
        print('Venta media')
        venta_Media += 1
    else:
        print('Venta menor')
        venta_Menor += 1
print('------------')
print('Resumen')
print('Vntas mayores: ', venta_Mayor)
print('Venta media: ', venta_Media)
print('Venta menor: ', venta_Menor)
print(f'Total de ventas: {total}')