intentos_fallidos = 0
clave = 5555
intentos = 3
int(input("Ingresa tu clave: "))
while clave != 5555:
    clave = 5555
    
    
    if clave != 5555:
        print(f"Clave incorrecta, te quedan {intentos} intentos.")
        intentos = intentos - 1
        intentos_fallidos = intentos_fallidos + 1
        
