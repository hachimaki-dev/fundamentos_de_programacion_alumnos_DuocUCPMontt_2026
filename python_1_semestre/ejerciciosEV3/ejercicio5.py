""" Ejercicio 5 — Código de producto en una bodega
Una bodega industrial registra productos por código. El código debe:

Tener al menos 6 caracteres
No tener espacios
Pide el código hasta que sea válido. Luego muestra:

"Producto registrado con código: PROD7X"
Ejercicio de análisis: ¿Qué función de Python usarías para detectar si hay espacios? Hay al menos dos formas distintas. Encuentra ambas. """


contador = 0
while contador == 0:
    codigo = input("ingrese el codigo: ").upper()
    tamano_minimo_letras = len(codigo)
    if tamano_minimo_letras >= 6 and " " not in codigo:
        print(f"Producto registrado con código: {codigo}")
        contador +=1
    
    else:
        print("respeta las reglas ")