codigo_respuesta = [200 , 404 , 500 , 200 ,500]
salvavidas = 1


for c in codigo_respuesta:

    if c == 200:
        print("OK")
    elif c == 404:
        print("NO ENCONTRADO")
    elif c == 500:
        salvavidas -= 1
        
        if salvavidas < 0:
            print("SERVIDOR CAIDO")
            break  
        else:
            print("REINTENTANDO")