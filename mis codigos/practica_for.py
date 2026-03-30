#A diferencia del while, en el for si es necesario determinar la cantidad de vueltas de alguna forma. el como depende de quien lo hace

#para contar del 0 al 10
for cada_elemento_dentro_de in range(10):
    print(f"\nhola vamos en el numero {cada_elemento_dentro_de}")

#para contar del 10 al 19
for cada_elemento_dentro_de in range(10,20):
    print(f"\nhola vamos en el numero {cada_elemento_dentro_de}")

#para contar del 10 al 19 de 3 en 3
for cada_elemento_dentro_de in range(10,20,3):
    print(f"\nhola vamos en el numero {cada_elemento_dentro_de}")

#para "saltar" la vuelta si se cumple la condición. en este caso, los numeros que al dividirse en 2 sean enteros(0,2,4) y muestra solo los demas (1,3,5)
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)


for i in range(6):
    if i == 4:
        break
    print(i)