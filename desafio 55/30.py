web = [200, 404, 500, 200, 500]
reintentos = 1

for web in web:
    if web == 200:
       print("Ok")
    if web == 404:
        print("No encontrado")
    if web == 500:
        reintentos -= 1  
        if reintentos < 0:
            print("Servidor caido")
            break
        print("reiciando")

    
    