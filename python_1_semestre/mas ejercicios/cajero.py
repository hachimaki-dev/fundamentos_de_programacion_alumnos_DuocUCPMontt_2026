#Objetivo: Simular un cajero con validación de seguridad.

#1. El usuario tiene un saldo fijo (ej. $50.000) y un PIN secreto predefinido (ej. 1234).
#2. Tiene máximo 3 intentos para ingresar el PIN usando un while.
#3. Si falla 3 veces, el programa termina de inmediato y muestra "Tarjeta bloqueada por seguridad".
#4. Si ingresa el PIN correcto, el ciclo de seguridad se corta, y pasamos al menú de retiro.
#5. Pregunta cuánto dinero quiere retirar.
#6. Usa un if para verificar:
#- Si el monto es mayor al saldo: "Fondos insuficientes".
#- Si el monto es igual a 0: "Monto inválido".
#- Si es válido, resta el dinero, y muestra "Retiro exitoso. Su nuevo saldo es: $X".


 
contador = 0
intentos = 3

clave = int(input("añade una clave: "))
saldo = int(input("cuanto dinero tienes en el cajero?: "))


while clave == clave:
    
    clave_cajero = int(input("ingrese su clave: "))
    contador = contador +1


    if contador == intentos:
        print("targeta bloqueada")
        break
    
    elif clave_cajero != clave:
        contador+1
        print("intente de nuevo")
        
    
    elif clave_cajero == clave:

        dinero_retiro = int(input(("menu: 1.cuanto dinero quieres retirar ?: ")))
        
        if dinero_retiro > saldo:
            print("fondos insuficientes")
            
        
        elif dinero_retiro == 0 :
            print(" monto invalido")
            
    
        elif dinero_retiro > 0 and dinero_retiro < saldo:
            saldo = saldo - dinero_retiro
            print(f"retiro exitoso. su nuevo saldo es: {saldo} ")
            break
            
    else: 
        print("no valido  ") (contador+1)
        continue
        
        