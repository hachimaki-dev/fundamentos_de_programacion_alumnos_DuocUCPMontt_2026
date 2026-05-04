#Crea una variable suma con valor 0 y una variable contador con valor 1. 
#Usa un ciclo while para que, mientras contador sea menor o igual a 5, se agregue contador a suma y luego contador aumente en 1.
# Al final, imprime suma.
suma = 0 
contador = 1
while contador <= 5:
    suma = suma + contador
    contador += 1
print(suma)