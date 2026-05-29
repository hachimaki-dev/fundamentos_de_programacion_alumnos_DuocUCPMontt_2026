print("###"*10)
print("CALCULADORA")
print("###"*10)

print()


while True:

    print()
    print("MENU:\n1 Sumar\n2 Restar\n3 Multiplicar\n4 Dividir")
    print()

    opcion = input("Ingrese la opcion a realizar :   ").lower().split()
    print()
    n1 = float(input("Ingrese un n1 : "))
    print()
    n2 = float(input("Ingrese un n2 : "))

    if opcion == "salir":
        print("Saliste de la Caculadora")
        break
    elif opcion == "sumar":
         def sumar(numero_1 , numero_2):
            return numero_1 + numero_2
         print(sumar(n1 , n2))
         break
    elif opcion == "restar":
         def resta(numero_1 , numero_2):
            return numero_1 - numero_2
         print(resta(n1 , n2))
         break
    elif opcion == "multiplicar":
         def multiplicar(numero_1 , numero_2):
            return numero_1 * numero_2
         print(multiplicar(n1 , n2))
         break
    elif opcion == "dividir":
         def dividir(numero_1 , numero_2):
            return numero_1 // numero_2
         print(dividir(n1 , n2))
         break
    else:
        print("Ingrese una Opcion Valida")
        break
        






