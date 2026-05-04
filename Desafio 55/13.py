ganancia_cliente = 800000
anios_en_banco = 6
numero_deudas = 0

eres_vip = ganancia_cliente > 1000000 or (anios_en_banco > 5 and numero_deudas == 0)

if eres_vip :
    print("Cliente VIP")
else :
    print("Cliente Normal")