#Funcion solo funciona a lo que mas importante , osea las responsabilidad mas pequeña
#Funcion recibe una entrada , se le conoce como argumento y entrara como parametro , que se transforma en una salida ,SOLO PALABRAS QUE NO ESTE RESERVADAS , INT , INPUT , WHILE NO!
#Para ejecutar la funcion yo tendria que invocar la funcion 
#Ojo con el orden , no puedo ir primero el argumento arriba por que si no , no ejecuta
#El triple de un numero 



#def el_triple_de_un_numero(numero_ingresado):
    #resultado = numero_ingresado * 3
    #return resultado
#el_triple_de_un_numero(55)



#Calculadora 

def sumar (numero_1 , numero_2):
    resultado = numero_1 + numero_2
    return resultado
def resta (numero_1 , numero_2):
    resultado = numero_1 - numero_2
    return resultado
def multiplicar(numero_1,numero_2):
    resultado = numero_1 * numero_2
    return resultado
def division(numero1,numero_2):
    resultado = numero_1 // numero_2
    return resultado
#while True:
    print("1 .Sumar")
    print("2 . Restar")
    print("3 . Multiplicar")
    print("4 . Dividir ")
    print("5 . Salir")
    if opcion == 1:
        #sumamos
        numero_1 = int(input("Ingrese numero 1 : "))
        numero_2 = int(input("Ingrese numero 2 : "))
        print(sumar(numero_1 , numero_2))
    elif opcion == 2:
        #restamos
        numero_1 = int(input("Ingrese numero 1 : "))
        numero_2 = int(input("Ingrese numero 2 :"))
    elif opcion == 3:
        #multiplicar
    elif opcion == 4:
        #dividir

#codigo boilerplate

# =============================================
# CALCULADORA CON FUNCIONES
# =============================================

# --- DEFINICION DE FUNCIONES ---

# Funcion que suma dos numeros y retorna el resultado
def sumar(numero_1, numero_2):
    resultado = numero_1 + numero_2  # guardo la suma en resultado
    return resultado                 # retorno el resultado hacia afuera

# Funcion que resta dos numeros y retorna el resultado
def restar(numero_1, numero_2):
    resultado = numero_1 - numero_2  # guardo la resta en resultado
    return resultado                 # retorno el resultado hacia afuera

# Funcion que multiplica dos numeros y retorna el resultado
def multiplicar(numero_1, numero_2):
    resultado = numero_1 * numero_2  # guardo la multiplicacion en resultado
    return resultado                 # retorno el resultado hacia afuera

# Funcion que divide dos numeros y retorna el resultado
def division(numero_1, numero_2):
    if numero_2 == 0:                        # primero reviso si el segundo numero es cero
        return "Error: division entre cero"  # si es cero, retorno un mensaje de error
    resultado = numero_1 / numero_2          # si no es cero, divido con seguridad
    return resultado                         # retorno el resultado hacia afuera

# Funcion que pide dos numeros al usuario y los retorna
# No tiene parametros porque los datos los genera el usuario con input()
def pedir_numeros():
    numero_1 = float(input("Ingresa el primer número: "))  # float permite decimales como 3.5
    numero_2 = float(input("Ingresa el segundo número: ")) # float permite decimales como 3.5
    return numero_1, numero_2  # retorno los dos numeros juntos hacia afuera

# =============================================
# MENU PRINCIPAL
# =============================================

# while True significa "repite esto para siempre"
# el ciclo solo se detiene cuando el usuario elige la opcion 5 (break)
while True:

    # Muestro el menu de opciones
    print("\n===== CALCULADORA =====")  # \n es un salto de linea
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    # Pido al usuario que elija una opcion
    # El resultado del input siempre es un numero entero , por eso 1 al 5
    opcion = int(input("\nElige una opción (1-5): ")

    # Reviso que opcion eligio el usuario y llamo a la funcion correspondiente
    if opcion == 1:                    # si eligio 1
        n1, n2 = pedir_numeros()         # pido los dos numeros
        print(f"Resultado: {sumar(n1, n2)}")        # llamo a sumar y muestro el resultado

    elif opcion == 2:                  # si eligio 2
        n1, n2 = pedir_numeros()         # pido los dos numeros
        print(f"Resultado: {restar(n1, n2)}")       # llamo a restar y muestro el resultado

    elif opcion == 3:                  # si eligio 3
        n1, n2 = pedir_numeros()         # pido los dos numeros
        print(f"Resultado: {multiplicar(n1, n2)}")  # llamo a multiplicar y muestro el resultado

    elif opcion == 4:                  # si eligio 4
        n1, n2 = pedir_numeros()         # pido los dos numeros 
        print(f"Resultado: {division(n1, n2)}")     # llamo a division y muestro el resultado

    elif opcion == 5:                  # si eligio 5
        print("¡Hasta luego!")           # me despido
        break                            # break detiene el while True y termina el programa

    else:                                # si escribio cualquier otra cosa
        print("Opción no válida. Intenta de nuevo.")  # aviso que no es valida y el menu vuelve a aparecer














#Tarea : Implementar esta calculadora con un menu
#MALO
#def suma (numero_1 , numero_2):
    #resultado = numero_1 + numero_2
    #return resultado
#opcion_ingresada = 0
#while opcion_ingresada != 6:
    
    #print("1 . Suma")
    #print("2 . Resta")
    #print("3. multiplica")
    #print("4 . division")
    #print("5 . salir")
    #opcion_ingresada = int(input("Ingrese opcion :"))
    #numero_1 = int(input("Ingrese numero"))
    #numero_2 = int(input("Ingrese otro numero"))
    #if opcion_ingresada == 1:
        #def sumar (numero_1 , numero_2):
            #resultado = numero_1 + numero_2
            #return resultado
    #elif opcion_ingresada == 2:
        #def resta(numero_1 , numero_2):
            #resultado = numero_1 - numero_2
            #return resultado
#print(resultado)