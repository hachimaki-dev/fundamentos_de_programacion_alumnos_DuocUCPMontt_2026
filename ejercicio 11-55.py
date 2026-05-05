# Crea un contador `intentos_fallidos` en 0
#Asume que escribiste la clave 'Admin123'.

clave_buena = "contraseña"
clave_escrita = "Admin123"
intentos_fallidos = 0

clave_escrita = input("Ingresa tu contraseña\n")
while True:
    if  clave_escrita == clave_buena:
        print("pasas correctamente")
    else:
        intentos_fallidos += 1
        print(f"intentos fallidos: {intentos_fallidos}")
        break