gana = 800000
lleva_trabajando = 6
deudas = 0

if gana > 1000000 or (lleva_trabajando >= 5 and deudas == 0) :
    print("CLIENTE VIP")
else:
    print("CLIENTE NORMAL")