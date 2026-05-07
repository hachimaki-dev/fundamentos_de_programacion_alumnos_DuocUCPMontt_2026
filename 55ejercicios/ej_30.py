# Ejercicio 30: Procesamiento Resiliente (AWS)

print("Sistema de monitoreo web")

codigos = [200, 404, 500, 200, 500]

reintentos = 1

for codigo in codigos:

    if codigo == 200:
        print("Ok")

    elif codigo == 404:
        print("No encontrado")

    elif codigo == 500:

        reintentos = reintentos - 1

        if reintentos < 0:
            print("Servidor Caído")
            break

        print("Reintentando")