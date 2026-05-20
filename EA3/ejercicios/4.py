#Crea mayor_de_tres(a, b, c) que reciba 3 números y retorne el mayor de ellos.

def mayor_que_yo_remix(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and b > c:
        return c
    elif a == b:
        if a > c:
            return a
        elif a < c:
            return c
    elif a == c:
        if a > b:
            return a
        elif a < b:
            return b    
    elif b == c:
        if b > a:
            return b
        elif b < a:
            return a
        


print (mayor_que_yo_remix(6,9,4))