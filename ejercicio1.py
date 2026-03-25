#hacer un algoritmo en diagrama d flujos y luego que lo vadle mi compañero, crear el codigo.

#adivinar un numero determinado entre 1 y 10 si el usuario se equivoca, volver a preguntar si el usuario acierta entoncces felicitarlo


numero_secreto = 5
numero_ingresado = 0

acierto = True

while acierto == True:
    numero_ingresado = int(input("Ingrese un numero entre el 1 y el 10: "))
    if numero_secreto == numero_ingresado:
        print("Has encontrado el numero, Yiiipie.")
        acierto = False
    else:
        print("nuh uh bro")