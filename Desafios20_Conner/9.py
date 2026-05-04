### Ejercicio 9: Sumar valores de una lista

#Define la lista `precios = [1000, 2500, 500]`. Crea una variable `total_pagar` con valor `0`. Recorre la lista con un ciclo `for`, suma cada precio a `total_pagar`
# e imprime el resultado final.

#**Resultado esperado en consola:**

#```text
#4000
#```

#---

precios=[1000, 2500, 500]
total_pagar=0

for i in precios:
    total_pagar=total_pagar+i
print(total_pagar)