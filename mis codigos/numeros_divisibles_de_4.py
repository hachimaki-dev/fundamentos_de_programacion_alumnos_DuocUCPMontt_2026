contador = 0

for i in range(1, 32):
        if i % 4 == 0:
            contador += 1

print ("**********************************")
print (f"Hay {contador} numeros divisibles por 4")
print ("**********************************")