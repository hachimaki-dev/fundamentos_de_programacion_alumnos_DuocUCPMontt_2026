### Ejercicio 13: Contar mayores de edad

#Define la lista `edades = [15, 18, 22, 12, 40]`. Crea una variable `mayores_edad` con valor `0`.
#Recorre la lista y suma `1` cada vez que encuentres un número mayor o igual a `18`. Imprime el contador.

#**Resultado esperado en consola:**

#```text
#3
#```

edades=[15, 18, 22, 12, 40]
contador=0
mayores_edad=0

for i in edades:
    if i>=18:
        contador=contador+1
        
print(contador)