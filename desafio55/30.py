web = [200, 404, 500, 200, 500]
reitento_salvavidas = 1
for i in web:
    if i == 200:
        print("OK")
    elif i == 404:
        print("NO ENCONTRADO")
    elif i == 500:
        reitento_salvavidas -= 1
        if reitento_salvavidas < 0:
            print("SERVIDOR CAIDO")
            break
        else:
            print("REITENTANDO")
