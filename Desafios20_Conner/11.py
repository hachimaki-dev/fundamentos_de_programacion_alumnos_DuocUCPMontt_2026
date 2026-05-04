### Ejercicio 11: Acceder a un dato del diccionario

#Define el diccionario `enemigo = {'nombre': 'Slime', 'hp': 45}`. Extrae el valor de la clave `'hp'`, guárdalo en una variable llamada `salud_actual` e imprime esa variable.

#**Resultado esperado en consola:**

#```text
#45
#```

enemigo={
    "nombre":"Slime",
    "hp": 45
}
salud_actual=enemigo["hp"]
print(salud_actual)