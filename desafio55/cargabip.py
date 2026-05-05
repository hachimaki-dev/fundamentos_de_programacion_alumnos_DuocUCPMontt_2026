# pasaje de micro vale 750 y metro a hora punta vale 850 y al final del dia hay una recarga de 3000
# 1 micro 2 metros
bip_inical = 10000
micro = 730
metro = 850
recarga = 3000
print(f"tu bip tiene un saldo de {bip_inical} mil pesos ,y el dia de hoy tomaste 1 micro de un valor de {micro} pesos para depues 2 dos pasajes de metro que en hora punta vale {metro} cada uno para terminar recargaste {recarga} mil pesos")

bip_inical = bip_inical - micro
bip_inical = bip_inical - metro*2
bip_inical = bip_inical + recarga
print(f"tu saldo queda en {bip_inical}")







