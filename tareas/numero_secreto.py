numero_secreto = 72
intentos = 0
numero_del_usuario = 0
print("bienvenido")
print("adivine el numero entre 1 y 100")
while numero_secreto != numero_del_usuario:
    numero_del_usuario = int(input("ingrese su numero"))
    if numero_del_usuario < numero_secreto:
        print (f"el numero es mayor que {numero_del_usuario}")
    elif numero_del_usuario > numero_secreto:
        print(f"el numero es menor que {numero_del_usuario}")
    intentos += 1

print("felicidades")
print("adivinaste")
print(f"numero de intentos fue {intentos}")