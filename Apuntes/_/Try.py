#Investigar para que sirve y como se usa la estructura de control de excepciones en python. (TRY EXCEPT)

#La estructura de control de excepciones en Python se utiliza para manejar errores o situaciones excepcionales que pueden ocurrir durante la ejecución de un programa.
#La sintaxis básica es la siguiente:

#try:
    # Código que puede generar una excepción
#except TipoDeExcepcion:
    # Código que se ejecuta si ocurre la excepción

#Dentro del bloque "try", se coloca el código que se espera que pueda generar una excepción.
#Si ocurre una excepción, el programa saltará al bloque "except" correspondiente, donde se puede manejar la excepción de manera adecuada.

#Ejemplo de uso:
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero no permitida.")

#En este ejemplo, se intenta dividir 10 por 0, lo cual genera una excepción de tipo ZeroDivisionError. 
#El bloque "except" captura esta excepción y muestra un mensaje de error en lugar de que el programa se detenga abruptamente.
#También es posible capturar múltiples tipos de excepciones utilizando varios bloques "except":
try:
    numero = int(input("Ingrese un número: "))
    resultado = 10 / numero
    print(f"El resultado de 10 dividido por {numero} es: {resultado}")
except ZeroDivisionError:
    print("Error: División por cero no permitida.")
except ValueError:
    print("Error: Entrada no válida. Por favor, ingrese un número entero.")

#A

while True:
    try:
        numero = int(input("Ingrese un número: "))
    except:
        print(f"Error: Entrada no válida. Por favor, ingrese un número entero.")
    else:
        print(f"El número ingresado es: {numero}")
        break

#Otro ejemplo:

numero1=100
numero2=0

try:
    resultado=numero1/numero2
except ZeroDivisionError:
    print("Error: División por cero no permitida.")
print(resultado)
