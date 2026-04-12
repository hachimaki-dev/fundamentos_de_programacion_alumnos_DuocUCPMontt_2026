#CANT DE ARMAS DE VALORANT
arma = 0

#CICLO DE ARMAS EN LA PARTIDA 
while arma < 5:
    arma += 1     #ESTO SUMA LAS ARMAS
    
    if arma == 4:
        print("Arma 4: Notificación - Agotada")
        continue
    
    print(f"Comprando exitosamente el arma número {arma}")
