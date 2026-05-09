cantidad_a_sacar = 37000
biletes = [20000 , 10000 , 5000 , 1000]

c = {}

for i in biletes:
    cuento_entran = cantidad_a_sacar // i

    if cuento_entran > 0:
        c[i] = cuento_entran

    cantidad_a_sacar = cantidad_a_sacar % i

print(c)
    

