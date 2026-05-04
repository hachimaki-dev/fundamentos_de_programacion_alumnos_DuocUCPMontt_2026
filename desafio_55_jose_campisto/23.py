intentos=0
clave="3ln4b0j0mas"
intento=""
while True:
    intento=input("ingrese su clave: ")
    if intento==clave:
        print("Bienvenido al cajero")
    else:
        print("intento fallido")
        intentos+=1
        if intentos == 3:
            print("tarjeta bloqueada")
            break