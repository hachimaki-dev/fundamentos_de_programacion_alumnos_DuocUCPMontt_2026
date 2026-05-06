print("Bienvenido a BancoEstado!")
print("Vamos a comprobar si cumple con los requisitos para volverse un cliente VIP")
print("Para volverse un cliente vip debes tener un sueldo mayor a 10000000 o llevar 5 años en el banco sin deudas")
sueldo_cliente = 800000
tiempo_en_banco = 6
deudas_cliente = 0

if sueldo_cliente > 10000000 or tiempo_en_banco >= 5 and deudas_cliente == 0:
    print("Requisitos cumplidos")
    print("Cliente promovido a la categoría VIP")
else:
    print("Cliente no cumple con los requisitos, se mantiene en cliente normal y pobre.")