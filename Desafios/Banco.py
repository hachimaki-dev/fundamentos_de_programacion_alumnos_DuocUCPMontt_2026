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


Saldo= 50000
PIN = 3698
ContadorIntentos = 0
Intento = 0
Retiro = False
Programa = True

while Programa == True:
    Intento = input("Ingrese su clave: ")
    
            
    if int(Intento) == PIN:
        Retiro = True
    else:
        ContadorIntentos += 1
        print ("Intente nuevamente")
        if ContadorIntentos >= 3:
            print ("Tarjeta Bloqueada por segurida")
            Programa = False
        
    
    

    while Retiro == True:
        print ("¿Cuanto dinero desea retirar?")
        DineroARetirar = int(input("Ingrese cifra a retirar: "))
        if DineroARetirar == 0:
            print("\nMonto inválido")
            print("\n Intente nuevamente")
        elif DineroARetirar > Saldo:
            print("\nFondos insuficientes")
            print("\n Intente nuevamente")
        else:
            Saldo = Saldo - DineroARetirar
            print (f"Retiro exitoso: \nUsted retiro \n${DineroARetirar} \ny su saldo actual es \n${Saldo}")
            Programa = False
            Retiro = False
            




print ("\nFin del programa")