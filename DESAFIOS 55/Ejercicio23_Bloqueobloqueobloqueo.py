intentos=0
while True:

    clave=input("")
    if clave=="break":
        break
    else:
        intentos+=1
    if intentos == 3:
        print("Bloqueo de tarjeta")
        break
    

