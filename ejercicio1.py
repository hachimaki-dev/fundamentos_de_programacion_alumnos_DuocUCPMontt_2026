#hacer un algoritmo en diagrama d flujos y luego q lo valide mi compañero, creal el codigo

#adivinar un numero determiado entre 1 y 10. Si el usuario se equivoca, volver a preguntar. Si el usuario acierta entonces, felicitarlo.

numero_secreto = 6
numero_ingresado = 0



while numero_secreto != numero_ingresado:
    numero_ingresado = int(input("ingrese numero: "))
    if numero_ingresado!=numero_secreto:
        print("vuleve a intentar")

print("adivinaste")
