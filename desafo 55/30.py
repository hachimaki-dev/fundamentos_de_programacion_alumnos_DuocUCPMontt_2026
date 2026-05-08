vida_extra = 1
lista = ["200, 400, 500, 200, 500"]

for codigo in lista:
    if codigo == 200:
        print("ok")
    elif codigo == 400: 
        print("No encontrado")
    else: 
        vida_extra = vida_extra - 1 

        if vida_extra > 0: 
            print("servidor caido")
            break 
        else: 
            print("Reintentando")
            

