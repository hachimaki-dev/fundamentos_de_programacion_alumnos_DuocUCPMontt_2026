cliente_gana = 800000
tiempo_en_banco = 6
deudas = 0
#lo que exigue el banco
sueldo_minimo = 1000000
tiempo_minimo = 5
deudas_maximas = 0
if cliente_gana >= sueldo_minimo or tiempo_en_banco >= tiempo_minimo and deudas <= deudas_maximas:
    print("cliente VIP")
else:
    print("faltan requisito por cumplir para ser cliente VIP")