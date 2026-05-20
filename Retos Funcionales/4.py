def mayor_de_tres(a,b,c):
    if a > b and a > c:
        return f"{a} es el mayor"
    elif b > a and b > c:
        return f"{b} es el mayor"
    elif c > a and c > b:
        return f"{c} es el mayor"

print((mayor_de_tres(5,4,3)))
print((mayor_de_tres(4,8,2)))
print((mayor_de_tres(15,10,20)))