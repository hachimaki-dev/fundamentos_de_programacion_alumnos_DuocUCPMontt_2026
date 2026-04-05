#aca se usa el "in" para poner esos valores determinados dentro de "numero ingresado"

numero_ingresado:0


numero_ingresado = int(input("ingrese un numero: "))
if numero_ingresado in [1,3,5,7,9]:
    print("IMPAR")

elif numero_ingresado in [2,4,6,8,10]:
    print("PAR")

print("LISTO")