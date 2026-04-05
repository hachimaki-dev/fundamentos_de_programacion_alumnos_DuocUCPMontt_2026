perros_de_paseo=int(input("Cantidad de perros que paseó hoy: "))
ganancia_total=0
perros_paseados=1

while perros_paseados<=perros_de_paseo:
    peso_perros=int(input("Ingrese el peso del perro que paseó en kg: "))
    if peso_perros<10:
        ganancia_total+=2000
        perros_paseados+=1
    elif 10<=peso_perros<25:
        ganancia_total+=4000
        perros_paseados+=1
    else:
        ganancia_total+=6000
        perros_paseados+=1
print(f"Resumen del día: Has paseado {perros_de_paseo} perros, ganando en total ${ganancia_total}")