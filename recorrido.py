print("===============================")
print("Bienvenidos al recorrido alerce")
print("===============================")

print("Bievenidos, seleccione al lugar que desea recorrer por el dia de hoy")
print("Pero antes, ingrese su nombre")

nombre_usuario = str(input ("Ingrese su nombre : "))

print ("Bienvedio " + nombre_usuario)
print ("contamos con los siguientes lugares para visitar")
print ("1. Puerto Mott a Alerce")
print ("2. Alerce a Puerto Montt")
print ("3. Calbuco a Puerto montt")

recorrido_elegido = int (input ("Seleccione el lugar de destino : "))
if recorrido_elegido == 1 :
    print(f" Usted ha seleccionado {recorrido1} su costo es de $ {precio_de_recorrido1}")
    confirmar_eleccion = int(input ("Confirme su destino con 1 o 2 : "))
    if confirmar_eleccion == 1 :
        print ("Confirmación recibida, que tenga un buen dia :) ")
    elif confirmar_eleccion == 2 :
        print ("Ha cancelado su destiono, que tenga un buen dia ; ) ")
    
    else : print ("Por favor seleccione un metedo mencionado anteriormente")

elif recorrido_elegido == 2 :
    print (f"Usted ha seleccionado {recorrido2} su costo es de $ {precio_de_recorrido2}")
    confirmar_eleccion = int(input ("Confirme su destino con 1 o 2 : "))
    if confirmar_eleccion == 1 :
        print ("Confirmación recibida, que tenga un buen dia :) ")
    elif confirmar_eleccion == 2 :
        print ("Ha cancelado su destiono, que tenga un buen dia ; ) ")

    else : print ("Por favor seleccione un metedo mencionado anteriormente")

elif recorrido_elegido == 3 :
    print (f"Usted ha seleccioan  {recorrido3} su costo $ {precio_de_recorrido3}")
    confirmar_eleccion = int(input ("Confirme su destino con 1 o 2 : "))
    if confirmar_eleccion == 1 :
        print ("Confirmación recibida, que tenga un buen dia :) ")
    elif confirmar_eleccion == 2 :
        print ("Ha cancelado su destiono, que tenga un buen dia ; ) ")

    else : print ("Por favor seleccione un metedo mencionado anteriormente")



recorrido1 = "Puerto Montt a Alerce"
recorrido2 = "Alerce a Puerto Montt"
recorrido3 = "Calbuco a Puerto Mott"

precio_de_recorrido1 = 2.00 
precio_de_recorrido2 = 3.00
precio_de_recorrido3 = 1.50