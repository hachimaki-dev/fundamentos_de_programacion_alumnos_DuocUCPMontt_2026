#que ingrese un numero
numero = int(input("ingrese un numero"))
#si numero es menor a 0 entonces:
if numero < 0:
    print("solo numero positivos")
#imprime con un for in del rango 1 al 10 los siguientes numeros , entonces es igual a numero por el numero dentro del ciclo controlado
else:
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")