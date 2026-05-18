# ponerle un menu de opciones 

def sumar(numero1, numero2):
    return numero1 + numero2
    


def restar(numero1, numero2):
    return numero1 - numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

def dividir(numero1, numero2):
    return numero1 // numero2

def solicitar_dos_numeros():
    numero1 = int(input("ingrese su primer numero: "))
    numero2 = int(input("ingrese su segundo numero: "))
    return(numero1, numero2)



while True:
    print("elige una opcion para usar la calculadora")
    print("1. suma")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    print("5. terminar")
    opcion_elegida = int(input("eliga que opcion va a ser: "))

    if opcion_elegida == 1 :
        numero1, numero2 = solicitar_dos_numeros()
        print(sumar(numero1, numero2))
    elif opcion_elegida == 2: 
       numero1, numero2 = solicitar_dos_numeros()
       print(restar(numero1, numero2))



    elif opcion_elegida == 3: 
        numero1, numero2 = solicitar_dos_numeros()
        print(multiplicar(numero1, numero2))
        

    elif opcion_elegida == 4:
        numero1, numero2 = solicitar_dos_numeros()
        print(dividir(numero1, numero2))


    elif opcion_elegida == 5: 
        print("saliendo")
        break

    else:
        print("opcion invalida")  
    
       

