### Ejercicio 6: Contador de letras

#Define la variable `palabra` con el valor `'manzana'`. Crea una variable `contador_a` con valor `0`. Recorre la palabra con un ciclo `for` y
# cada vez que encuentres la letra `'a'`, suma `1` al contador. Al final, imprime `contador_a`.

#**Resultado esperado en consola:**

#```text
#3
#```

#---

palabra="manzana"
contador=0

for a in palabra:
    if "a"==a:
        contador=contador+1
print(contador)