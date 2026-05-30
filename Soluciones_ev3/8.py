mayores = 0
medias = 0
menores = 0
total = 0 

for i in range (1,7):
    monto = int(input(f"Ingrese el monto de la venta {i}: "))
    total += monto

    if monto > 50000:
        print("Venta mayor")
        mayores += 1
    elif 10000 <= monto <= 50000:
        print("Venta media")
        medias += 1
    else:
        print("Venta menor")
        menores += 1
    
print(f"Ventas Mayores: {mayores}")
print(f"Ventas Medias: {medias}")
print(f"Ventas Menores: {menores}")
print(f"Total de Ventas: {total}")

