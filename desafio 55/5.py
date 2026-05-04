plata_tarjeta = 10000
pasaje_micro = 730
pasaje_metro = 850
recarga = 3000

saldo_despues_de_tomar_micro_y_metro = (plata_tarjeta - pasaje_micro - pasaje_metro - pasaje_metro)

saldo_final = (saldo_despues_de_tomar_micro_y_metro + recarga)


print("En este dia tomaras 1 micro y 2 metros, por ende calcularemos en cuanto quedara tu saldo de tarjeta BIP al final del dia.")

input()

print(f"Tu saldo actual es de {plata_tarjeta}.")

input()

print(f"Despues de tomar la micro y los 2 pasajes de metro te quedan {saldo_despues_de_tomar_micro_y_metro}.")

input()

print(f"Piensas en recargar un poco mas d eplata por si acaso, por ende le recargas 3000 pesos mas quedando tu tarjeta con: {saldo_final}. ")