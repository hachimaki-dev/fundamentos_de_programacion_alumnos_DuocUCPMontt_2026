sueldo = 800000
años = 6
deudas = 0 

plata = int(input("Cuando dinero gana usted: "))
tiempo = int(input("cuantos años lleva en el banco: "))
debe = int(input("cuantas deudas tiene: "))


if plata >= 1000000 or tiempo >= 5 and debe == 0: 
    print("Cliente VIP")

else: 
    print("Cliente Normal")
