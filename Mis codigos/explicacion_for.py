# A diferencia del while en el for si es necesario determinar la cantidad de vueltas de alguna forma
# for CADA_ELEMENTO_QUE_SE_ENCUENTRA_DENTRO_DE_OTRO_CONJUNTO_DE_ELEMENTOS -> i
# range(1 valor) comienza desde 0

#EJ 1
# for cada_elemento_dentro_de in range(5):
#     print(f"hola vamos en el numero {cada_elemento_dentro_de}")

#EJ2
# for cada_elemento_dentro_de in range(10,20):
#     print(f"hola vamos en el numero {cada_elemento_dentro_de}")

#EJ3
# for cada_elemento_dentro_de in range(2,15,3):
#     print(f"hola vamos en el numero {cada_elemento_dentro_de}")

#EJ4
# continue: salta los pares
# continue sigue a la siguiente iteracion, vuelve al for
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)  # Imprime: 1,3,5