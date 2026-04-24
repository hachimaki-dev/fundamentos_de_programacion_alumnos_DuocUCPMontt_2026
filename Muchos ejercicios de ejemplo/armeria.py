contador_arma = 0

while contador_arma <= 5 :
    contador_arma += 1

    if contador_arma == 4 or contador_arma == 2:
        print(f"Arma {contador_arma}: Notificacion - Agotada.")
        continue

    print (f"comprando exitosamnete el arma numero [{contador_arma}].")