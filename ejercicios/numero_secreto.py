Numero_secreto = 67
Intentos = 0
print("bienvenido al numero secreto")
Respuesta = int(input("ingrese su numero"))
while Respuesta != Numero_secreto :
    print("error vuelve a intentarlo")
    Intentos = Intentos + 1
    if Respuesta > Numero_secreto :
        print("el numero secreto es mas bajo")
    elif Respuesta < Numero_secreto :
        print("el numero secreto es mas alto")
    Respuesta = int(input("ingrese un numero"))
    
print(f"felicidades lo lograste en {Intentos} intentos")
print("fin")