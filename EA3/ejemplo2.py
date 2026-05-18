def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 // num2

def solicitar_dos_numeros():
    num1= int(input("Ingrese un numero para trabajar: "))
    num2= int(input("Ingrese otro numero para trabajar: "))
    return num1, num2

while True:
    print("---Seleccione que quiere hacer en la calculadora de python---")
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Salir ")
    seleccion_usuario=int(input("Seleccione una de las opciones: "))
    if seleccion_usuario==5:
        print("Saliendo del codigo")
        break
    if seleccion_usuario==1:
        num1,num2=solicitar_dos_numeros()
        print( suma(num1, num2))
    elif seleccion_usuario==2:
        num1,num2=solicitar_dos_numeros()
        print( resta(num1, num2))
    elif seleccion_usuario==3:
        num1,num2=solicitar_dos_numeros()
        print( multiplicacion(num1, num2))
    elif seleccion_usuario==4:
        num1,num2=solicitar_dos_numeros()
        
        print( division(num1, num2))
    else:
        print("Opcion invalida, Intente nuevamente con un numero valido")