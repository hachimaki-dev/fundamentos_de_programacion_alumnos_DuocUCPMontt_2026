 #Revisa si un cliente puede subir a categoría VIP en su banco

sueldo_del_cliente = int(input("porfavor ingrese su sueldo: ") )

tiempo_en_el_banco = int(input(" porfavor ingrese cuantos años lleva en el bamco: "))

deudas_activas = int(input("porfavor ingrese cuantas deudas tiene: "))

if sueldo_del_cliente > 1000000 or (tiempo_en_el_banco >= 5 and deudas_activas == 0):
    
    print(f" felicidades usted a subido a categoria vip")
else: 
    print("cliente normal")
