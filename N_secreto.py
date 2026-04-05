numero_secreto = 1984 #por que dragon ball fue creado en ese año
intentos = 0
respuesta = ""

while respuesta != numero_secreto:
    respuesta = int(input("escribe el numero secreto, si crees saberlo..... "))
    intentos += 1
    if respuesta < numero_secreto:
        print("ERROR, El número es más ALTO")
    elif respuesta > numero_secreto:
        print("ERROR, El número es más BAJO")

print(f"Ganaste en {intentos} intentos, FELICIDADES!!!!")