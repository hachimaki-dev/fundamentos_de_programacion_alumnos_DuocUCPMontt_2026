cantidad_perros = int(input("¿Cuantos perros paseó en total el día de hoy? "))
contador_cantidad_perros = 1
valor_monetario_final = 0
while cantidad_perros >= contador_cantidad_perros:
    peso_del_perro = int(input(f"¿Cuantos kilos pesaba el perro N°{contador_cantidad_perros}? "))
    if peso_del_perro < 10:
        valor_monetario_final = valor_monetario_final + 2000
        contador_cantidad_perros = contador_cantidad_perros + 1
    elif peso_del_perro > 25:
        valor_monetario_final = valor_monetario_final + 6000
        contador_cantidad_perros = contador_cantidad_perros + 1
    else:
        valor_monetario_final = valor_monetario_final + 4000
        contador_cantidad_perros = contador_cantidad_perros + 1
print(f"Resumen del día: Has paseado {cantidad_perros} perros ganando en total ${valor_monetario_final}")