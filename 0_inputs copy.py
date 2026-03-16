#La funcion input permite al usuario ingresar datos por teclado

#Se pueden guardar valores

print ("Bienvenido a calculadora 2000")

operacion = input ("¿Que operacion desea realizar? suma, resta, multiplicacion o division? ")
if operacion == ("suma"):
    then print
numero_1 = input ("ingrese numero 1: ") 

numero_2 = input ("ingrese numero 2: ") 

resultado = int(numero_1) + int(numero_2)

print ("el resultado es ")
print (resultado)