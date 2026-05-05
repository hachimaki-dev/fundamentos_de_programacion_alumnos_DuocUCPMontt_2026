#Ejercicio 11: Clave Única Básico

intentos_fallidos = 0
clave_correcta = "secreto"


while True:
    clave = input("¿Cual es su clave?")

    if clave == clave_correcta:
        print("Entraste")
        break
    else:
        print("clave incorrecta")
        intentos_fallidos += 1 
        print(f"Intentos fallidos: {intentos_fallidos}")