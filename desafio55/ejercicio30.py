respuesta_web = [200,404,500,200,500]
reintento = 1
for i in respuesta_web:
    if i == 200:
        print("Ok")
    elif i == 404:
        print("No encontrado")
    elif i == 500 and reintento == 1:
        reintento = reintento - 1
        print("Reintentando")
    elif i == 500 and reintento == 0:
        print("Servidor caido")
        break
    
