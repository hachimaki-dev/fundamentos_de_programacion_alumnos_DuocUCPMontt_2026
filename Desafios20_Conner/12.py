### Ejercicio 12: Sumar los valores de un diccionario

#Define el diccionario `ventas = {'taza': 500, 'plato': 1200, 'vaso': 300}`. Crea una variable `total_ventas` con valor `0`.
#Recorre los valores del diccionario, súmalos y luego imprime el total.

#**Resultado esperado en consola:**

#```text
#2000
#```

#---

ventas={
    "taza": 500,
    "plato": 1200,
    "vaso": 300
}

total_ventas=0
for i in ventas.values():
    print(i)
    total_ventas=total_ventas+i
print(total_ventas)