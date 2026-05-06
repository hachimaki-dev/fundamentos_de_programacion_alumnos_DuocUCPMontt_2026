#Crea una lista llamada `alumnos` que contenga estos dos diccionarios:

#```python
#{'nombre': 'Ana', 'nota': 5.0}
#{'nombre': 'Luis', 'nota': 3.0}
#```

#Luego, cuenta cuántos alumnos tienen una nota mayor o igual a `4.0` y guarda ese valor en una variable llamada `aprobados`. Imprime `aprobados`.

#**Resultado esperado en consola:**

#```text
#1
#```

alumnos=[{"nombre": "Ana",
           "nota": 5.0},
            {"nombre": "Luis",
             "nota": 3.0} ]

aprobados=0

for i in alumnos:
    if i["nota"]>=4.0:
        aprobados=aprobados+1

print(aprobados)