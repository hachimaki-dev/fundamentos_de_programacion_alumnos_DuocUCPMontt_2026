web = [200,404,500,200,500]
reintento = 1

for i in web :
    if i == 200 :
        print("Ok")
    elif i == 404 :
        print("No encontrado")
    elif i == 500 :
        print("Reintentando")
        reintento-= 1
        
        if reintento < 0 :
            print("Servidor caido")
            break
            print("Reintentando")