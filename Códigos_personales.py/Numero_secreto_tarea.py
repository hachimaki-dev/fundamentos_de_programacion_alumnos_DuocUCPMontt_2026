numero_secreto = 50
numero_usuario = 0
numero_intentos = 0

print("""   A  D  I  V  I  N  A 
    EL NUMERO SECRETO""")

while numero_usuario != numero_secreto:
    numero_usuario = int(input("Ingrese un número "))
    numero_intentos = numero_intentos + 1
    print("PROCESANDO... O___<")
    if numero_usuario != numero_secreto:
        if numero_usuario > numero_secreto:
            print("Su numero es muy alto... Intente de nuevo")
        else:
            print("El numero ingresado es muy bajo... Intente otra vez")
    if numero_usuario == numero_secreto:
        print(f"HA ADIVINADO, EL NUMERO CORRECTO ES: {numero_secreto}")
print("FELICIDADES")
if numero_intentos == 1:
    print(f"Ha ganado en {numero_intentos} intento")
else:
    print(f"Ha ganado en {numero_intentos} intentos")