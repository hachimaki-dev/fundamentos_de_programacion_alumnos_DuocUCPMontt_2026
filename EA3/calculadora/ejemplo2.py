def suma(numero_1 , numero_2):
    return numero_1 + numero_2

def resta(numero_1 , numero_2):
    return numero_1 - numero_2

def multiplicacion(numero_1 , numero_2):
    return numero_1 * numero_2

def division(numero_1 , numero_2):
    return numero_1 // numero_2

print(suma(5,2))
print(resta(5,2))
print(multiplicacion(5,2))
print(division(5,2))


#tarea hacer menu interactivo 1 es suma, 2 es resta, 3 multiplicacion, 4 division, 5 salir, y cualquier otro numero es una opcion invalida

while True:
    print("1. sumar..")
    print("2. restar..")
    print("3. multiplicar..")
    print("4. division..")
    print("5. salir..")
    opcion = int(input("elige una opcion.."))
    if opcion == 1:
        num1= int(input("elige el primer numero 1 "))
        num2 = int(input("elige el segundo numero  "))
        print(suma(num1,num2))
    elif opcion == 2:
        num1= int(input("elige el primer numero 1 "))
        num2 = int(input("elige el segundo numero  "))
        print(resta(num1,num2))
    elif opcion == 3:
        num1= int(input("elige el primer numero 1 "))
        num2 = int(input("elige el segundo numero  "))
        print(multiplicacion(num1,num2))  
    elif opcion == 4:  
        num1= int(input("elige el primer numero  "))
        num2 = int(input("elige el segundo numero "))
        print(division(num1,num2)) 
    elif opcion == 5:
        break

    else: 
        print("ingrese un numero valido..")




#transformar el ejercicio uno o el jercicio 2 de la prueba a progrmacion funcional 






    

