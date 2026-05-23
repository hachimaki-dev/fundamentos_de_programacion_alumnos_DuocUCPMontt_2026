def mayor_de_tres(a,b,c):
    if a > b > c:
        print(a)
    elif a < b > c:
        print(b)
    elif a < b < c:
        print(c)

a = int(input("numero 1: "))
b = int(input("numero 2: "))
c = int(input("numero 3: "))

mayor_de_tres(a,b,c)