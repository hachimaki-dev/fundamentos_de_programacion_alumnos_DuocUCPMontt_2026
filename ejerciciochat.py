from random import randint

base=1000
techo=9999

clave=randint(base, techo)
#print(clave)     #CUALQUIER NUMERO EN ESE RANGO

#while clave%2!=0:
#    clave=randint(base, techo)
#print(clave)     #PARA QUE SEA PAR DENTRO DEL RANGO

while clave%10!=0:
    clave=randint(base, techo)
print(clave)     #PARA QUE ADEMAS SEA EN TERMINACION 0


acerto=False
intento=0

while acerto==False:

    while intento<5:  

        intento=intento+1
        clave_user=int(input("Ingrese la clave "))
        
        if intento==5:
            break

        if clave_user<clave:
            print("La contraseña es mayor ")
        elif clave_user>clave:
            print("La contraseña es menor")
        else:
            print(f"\nAcertaste en {intento} intentos\n")
            acerto=True
            break
    
    else:
        print(f"\nPerdiste en {intento} intentos\n")
        break
