lista = [200, 404, 500, 200, 500]

intentos = 1

for lista in lista:
    if lista == 200:
        print("ok")

    elif lista == 404:
        print ("no encontrado") 

    elif lista == 500:
        intentos = intentos - 1
        
        if intentos < 0:
            print("servidor caido") 
            break
        print("reintentando")   

hola


    

    