numero_secreto = 7

numero_elegido = int(input("Bienvenido/a, ingrese su numero del 1 al 10"))

while numero_secreto != numero_elegido:
    print("Incorrecto vuelva a intentar")
    numero_elegido = int(input("Bienvenido/a, ingrese su numero del 1 al 10"))
    if numero_elegido == numero_secreto :
        break

print("Felicidades logro adivinar el numero")
    
