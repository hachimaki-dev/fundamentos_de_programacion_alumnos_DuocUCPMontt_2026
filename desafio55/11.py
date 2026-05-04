
intentos_fallidos = 0
clave = "admin123"
while intentos_fallidos < 3:
    print("--ingrese clave--")
    clav_ingresada = input("--")
    if clav_ingresada == clave:
        print("--Bienvenido--")
        break
    else:
        intentos_fallidos += 1
        print(f"intentos fallidos {intentos_fallidos}")
        
        


