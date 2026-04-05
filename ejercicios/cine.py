print("bienvenido")
import sys
contraseña = 7089
dinero = 50000
intentos = 1
respuesta = int(input(f"ingrese su contraseña , si falla tiene 3 intentos. intento numero {intentos}     "))

while respuesta != contraseña :
    print("contraseña incorrecta")
    if intentos == 3:
        print("demasiados intentos fallidos, targeta bloqueada por seguridad")
        sys.exit()
    
    intentos = intentos + 1
    print(f"intento numero {intentos}")
    respuesta = int(input("ingrese su contraseña"))
    
print("contraseña correcta")    

retiro = int(input("cuanto dinero quiere retirar"))
if retiro > dinero :
    print("saldo insuficiente")
elif retiro == 0 :
    print("monto invalido")
elif retiro <= dinero :
    print("retiro exitoso")
    dinero = dinero - retiro
    print(f"en su cuenta queda {dinero} ")
    ###no le pedi el codigo a chatgpt busq eso del sys xdd