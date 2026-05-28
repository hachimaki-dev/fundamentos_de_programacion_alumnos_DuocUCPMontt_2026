# Ejercicio 5 — Código de producto en una bodega
# Una bodega industrial registra productos por código. El código debe:

# Tener al menos 6 caracteres
# No tener espacios
# Pide el código hasta que sea válido. Luego muestra:

# "Producto registrado con código: PROD7X"
# Ejercicio de análisis: ¿Qué función de Python usarías para detectar si hay espacios? Hay al menos dos formas distintas. Encuentra ambas.

while True:
    registro_de_producto = input("Ingrese el código del producto: ")

    tiene_espacios = False

    for caracteres in registro_de_producto:
        if caracteres == " ":
            tiene_espacios = True

    if tiene_espacios == True:
        #if " " in registro_de_producto:
        print("El código del producto no debe tener espacios.")

    elif len(registro_de_producto) < 6:
        print("El código del producto debe tener al menos 6 caracteres.")
    
    else:
        print(f"Producto registrado con código: {registro_de_producto}")
        break
