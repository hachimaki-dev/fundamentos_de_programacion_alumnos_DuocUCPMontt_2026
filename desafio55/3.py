amigo_total = 5
pinchanga_total = 15000 * 2
schops_total = 3500 * 5

#total consumo
total_consumo = (pinchanga_total + schops_total)
total_consumido_final = total_consumo  + (total_consumo * 0.1)
#consumo de amigos
consumo_amigos = (total_consumido_final // amigo_total)
print(f" El total a cancelar por cada uno es de {consumo_amigos}")