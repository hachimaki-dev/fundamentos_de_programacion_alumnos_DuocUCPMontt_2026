JH = 1000

print("****Bienvenido al la pelea final, tendras que pelear con JH, veamos si tienes lo necesario para derrotarlo****")

while JH > 0:
    daño = int(input("Ingresa el daño de tu arma:  "))

    if daño < 0:
        print(" JH esquivó tu  ataque, intentalo denuevo")
    else:
        JH -= daño
        print("A JH le queda: ", JH)

    if JH <= 0:
        print("DERROTASTE A JH, felicidades, ahora eres el más jupi de los jupi")
        break