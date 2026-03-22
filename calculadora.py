#la variable opcion siempre empieza desde el numero 0
#el comando while sirve repetir un bloque de codigo mientras la condicion sea True
#Repite todo lo que está aquí adentro mientras el usuario NO elija la opción 5 que en este no hay nada pero se podria colocar para reiniciar el programa pero ya de por si lo hace de forma automatica
opcion = 0
while opcion != 5:
    print("-----Calculadora-----")
    print("Presione 1 para SUMAR")
    print("Presione 2 para RESTAR")
    print("Presione 3 para MULTIPLICAR")
    print("Presione 4 para DIVIDIR")
    opcion = int(input("Ingrese opción:"))
    if opcion == 1:
        #Sumar
        print("Ingreso a SUMAR")
        suma1 = float(input("Ingrese el primer valor : "))
        suma2 = float(input("Ingrese el segundo valor: "))
        resultado1 =  suma1 + suma2
        print(f"Resultado obtenido : {resultado1}")
    elif opcion == 2:
        #RESTAR
        print("Ingreso a RESTAR")
        resta1 = float(input("Ingrese el primer valor: "))
        resta2 = float(input("Ingrese el segundo valor: "))
        resultado2 = resta1 - resta2
        print(f"Resultado obtenido : {resultado2}")
    elif opcion == 3:
        #MULTIPLICAR
        print("Ingreso a MULTIPLICAR") 
        multiplicar1 = float(input("Ingrese el primer valor: "))
        multiplicar2 = float(input("Ingrese el segundo valor: "))
        resultado3 = multiplicar1 * multiplicar2
        print(f"Resultado obtenido : {resultado3}")
    elif opcion == 4:
        #DIVIDIR
        print("Ingreso a DIVIDIR")
        dividir1 = float(input("Ingrese el primer valor : "))
        dividir2 = float(input("Ingrese el segundo valor :"))
        resultado4 = dividir1 / dividir2 
        print(f"Resultado obtenido : {resultado4}")

#Float por que por una extraña razon cuando coloco int se transforma en numeros negativos , en una calculadora tambien se calcula como decimales ciertas operaciones