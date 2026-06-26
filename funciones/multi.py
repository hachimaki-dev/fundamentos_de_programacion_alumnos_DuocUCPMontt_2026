def tablademultiplicar(n1,n2):
    return str(n1) + " * " + str(n2) + " = " + str(n1*n2)

n = int(input("Ingrese un numero entero: "))
for i in range(0,13):
    print(tablademultiplicar(n,i))