contador = 0
bandera =  True

while bandera == True : 
    print(f"Hola mundito vamos en el número {contador}")

    contador = contador + 1 

    if contador == 10 :
        bandera = False 
        print(" Entre en el if del while y cambie la bandera")

print("sali del ciclo")


#opcion = int(input("ingrese número"))
#contador = 0
#while opcion == 1 :
#    contador += 1
#    print(f"hola mundo{ contador}")
#opcion = int(input("ingrese número"))
#while True:
    #hago cosas