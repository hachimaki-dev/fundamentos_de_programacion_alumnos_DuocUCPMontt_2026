bandera = True
contador = 0
print ("Hola")
while bandera == True :
    
    contador = contador+1 

    print (f"Contando  {contador}")

    if contador == 10:
        print("hemos llegado al final")
        bandera = False
print (f"Estanos fuera y la bandera vale:{contador}")

