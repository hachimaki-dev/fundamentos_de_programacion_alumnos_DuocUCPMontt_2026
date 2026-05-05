#: El cliente gana 800000
#lleva 6 años en el banco y tiene 0 deudas.
#Eres VIP si cumples UNA de estas dos opciones: Opción A) Ganas más de 1000000.
#  Opción B) Llevas 5 o más años en el banco Y tienes 0 deudas.

cliente_gana = int(input("ingresa tu sueldo: "))
tiempo_en_el_banco = int(input("años en el banco: "))
deudas = int(input("Cuantas deudas tienes?: ")) 

if cliente_gana > 1000000 or (tiempo_en_el_banco >= 5 and deudas == 0):
    print("CLIENTE VIP")
else:
    print("Cliente normal")