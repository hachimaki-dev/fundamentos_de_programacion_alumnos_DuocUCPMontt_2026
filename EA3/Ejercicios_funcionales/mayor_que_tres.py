def cualesmayor(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    if a == b or a == c:
        print("dos o mas numeros son iguales")