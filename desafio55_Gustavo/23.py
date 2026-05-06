contador = 0
clave = "1234"

while True :
    clave_ingreso = input("Ingrese su clave: ")

    if clave_ingreso != clave :
        contador += 1
        if contador == 3 :
            break
print("Tarjeta bloqueada")
