#Define la lista edades = [15, 18, 22, 12, 40]. Crea una variable mayores_edad con valor 0. 
# Recorre la lista y suma 1 cada vez que encuentres un número mayor o igual a 18. Imprime el contador.
edades = [15, 18, 22, 12, 40]
mayores_edad = 0 
for edad in edades:
    if edad >= 18:
        mayores_edad += 1
print(mayores_edad)