cliente_gana=800000
años_en_el_banco=6
deudas=0
if cliente_gana>1000000 or (años_en_el_banco>=5 and deudas==0):
    print("Cliente VIP")
else:
    print("Cliente Normal")