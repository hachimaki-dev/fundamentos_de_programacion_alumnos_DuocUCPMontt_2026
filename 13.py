#aprobacion credito 

sueldo_del_cliente = int(input("Ingrese su sueldo: "))
deudas_activas = int(input("Ingrese la cantidad de deudas activas: "))

if sueldo_del_cliente > 550000 and deudas_activas == 0:
    print("credito aprobado")
else:
    print("credito rechazado")


