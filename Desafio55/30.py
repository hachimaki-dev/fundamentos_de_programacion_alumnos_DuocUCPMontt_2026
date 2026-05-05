cod_web = [200, 404, 500, 200, 500]
reintento = 1
for cod in cod_web:
    if cod == 200:
        print("OK")
    elif cod == 404:
        print("No encontrado")
    else:
        reintento -= 1
        if reintento < 0:
            print("Servidor caido")
            break
        else:
            print("Reintentando")