sueldo = 550000 
deuda_activa = 1 

sueldo = int(input("Ingrese su sueldo: "))
deuda = int(input("Ingrese numero de deudas activas: "))

if sueldo >= 500000 and deuda == 0: 
    print("Aprobado")

else: 
    print("Rechazado")
