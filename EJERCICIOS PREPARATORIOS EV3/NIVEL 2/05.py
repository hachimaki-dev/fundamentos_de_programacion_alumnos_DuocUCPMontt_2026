#Ejercicio 5 — Código de producto en una bodega
#Una bodega industrial registra productos por código. El código debe:

#Tener al menos 6 caracteres
#No tener espacios
#Pide el código hasta que sea válido. Luego muestra:

#"Producto registrado con código: PROD7X"
#Ejercicio de análisis: ¿Qué función de Python usarías para detectar si hay espacios? Hay al menos dos formas distintas. Encuentra ambas.

while True:

    try:
        codigo_producto = input("Ingrese código del producto: ").upper()

        if len(codigo_producto) >= 6 and " " not in codigo_producto:
            print(f"Producto registrado con código: {codigo_producto}")
            break
        else:
            raise ValueError
    
    except ValueError:
        print("Código inválido.")