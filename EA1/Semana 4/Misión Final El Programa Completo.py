numero_elegido = int(input("Ingrese su numero del 1 al 10: "))
if numero_elegido in [1, 3, 5, 7, 9]:
    print("Numero Impar")
elif numero_elegido in [2, 4, 6, 8, 10]:
    print("Numero Par")
else:
    print("Fuera de rango") 