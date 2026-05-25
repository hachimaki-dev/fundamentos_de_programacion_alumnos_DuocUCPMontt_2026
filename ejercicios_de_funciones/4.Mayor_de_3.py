def mayor_de_tres(a, b, c):
    if a >= b and a >= c:
       return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
print(mayor_de_tres(20, -5, 14.9))

################################################################################

#def mayor_de_tres(a, b, c):
#    return max(a, b, c)
#
#print(mayor_de_tres(20, -5, 14.9))