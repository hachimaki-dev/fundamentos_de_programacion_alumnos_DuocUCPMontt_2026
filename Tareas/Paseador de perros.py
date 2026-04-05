Perros_paseados = 0
menos_de_10 = 0
entre_10_y_25 = 0
mas_de_26 = 0
menos_de_10_precio = 0
entre_10_y_25_precio = 0
mas_de_26_precio = 0
contador_total = 0
bandera = True
print("Eres un amante de los perros y trabajas paseandolos. Tu tarifa se basa en el peso del perro")
print("Por uno que pese entre 9 o menos cobras $2000 CLP")
print("Por uno que pese entre 10 y 25 cobras $4000 CLP")
print("Y por uno que pese más de 26 cobras $6.000 CLP")

print("Tu jornada ya termino y vas a sacar cuentas de lo que has generado, pero empecemos por lo básico")
Perros_paseados = int(input("¿Cuantos perros has paseado el dia de hoy?"))

while bandera:
    contador_total = contador_total + 1
    respuesta_1 = int(input(f"Cuanto pesaba el perro {contador_total} (Solamente introducir el numero, NO PONER KG)"))
    if respuesta_1 <= 9:
        menos_de_10 = menos_de_10 + 1
        menos_de_10_precio = menos_de_10_precio + 2000
    elif respuesta_1 >= 10:
        entre_10_y_25 = entre_10_y_25 + 1
        entre_10_y_25_precio = entre_10_y_25_precio + 4000
    else:
        mas_de_26 = mas_de_26 + 1
        mas_de_26_precio = mas_de_26_precio + 6000
    if contador_total == Perros_paseados:
        bandera = False
print(f"En total haz paseado a {menos_de_10} que pesaban 10KG o menos")
print(f"{entre_10_y_25} que pesaban entre 10K y 25G")
print(f"y {mas_de_26} que pesaban mas de 26Kg")
print(f"En total haz ganado ${menos_de_10_precio + entre_10_y_25_precio + mas_de_26_precio} CLP")
    