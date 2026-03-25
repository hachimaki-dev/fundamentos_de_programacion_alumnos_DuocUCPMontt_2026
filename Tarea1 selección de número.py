#Inicio
número_secreto = 8
número_escogido = int(input("Escoge un número entre el 1 y el 10"))
while número_escogido != número_secreto :
    print("Número incorrecto, Vuelve a intentar.")
    número_escogido = int(input("Elige un número."))
    if número_escogido == número_secreto :
        break
print("Felicidades haz acertado")
