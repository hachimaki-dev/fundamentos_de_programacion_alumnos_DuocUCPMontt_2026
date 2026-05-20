
def mayor_de_tres(n1,n2,n3):
    if n1>n2>n3:
        return print(n1)
    elif n1<n2>n3:
        return print(n2)
    elif n1<n2<n3:
        return print(n3)
print("Ingrese 3 numeros y dire el mas grande")
nr1 = int(input("ingrese un numero   "))
nr2 = int(input("ingrese un numero   "))
nr3 = int(input("ingrese un numero   "))
mayor_de_tres(nr1,nr2,nr3)
