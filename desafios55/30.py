lista_codigos = [200,404.500,200,500]

salvavidas = 1 

for i in lista_codigos :

    if i == 200 : 
        print("Ok")
    if i == 404 :
        print("No encontrado")
    if i == 200 :
        
        print("Reintentando")
        salvavidas = salvavidas - 1
    if salvavidas < 0 :
        print("Servidor Caido")  
        break
