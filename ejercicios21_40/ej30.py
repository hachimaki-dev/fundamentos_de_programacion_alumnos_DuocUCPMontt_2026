codigos = [200, 404, 500, 200, 500]
reintento = 1
for respuesta in codigos:
    if respuesta == 200:
        print("ok")
    
    elif respuesta == 404:
        print("no encontrado")
    
    elif respuesta == 500:
        reintento -= 1
    
        if reintento < 0:
            print("servidor caido")
            break
        print("reintentando")