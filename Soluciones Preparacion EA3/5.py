#Ejercicio 5 — Código de producto en una bodega
#Una bodega industrial registra productos por código. El código debe:

#Tener al menos 6 caracteres
#No tener espacios
#Pide el código hasta que sea válido. Luego muestra:

#"Producto registrado con código: PROD7X"
#Ejercicio de análisis: ¿Qué función de Python usarías para detectar si hay espacios? Hay al menos dos formas distintas. Encuentra ambas.



while True:
    codigo_bodega=input("\nIngrese el código del producto: ")
    tiene_espacios=any(caracter.isspace() for caracter in codigo_bodega)

    if len(codigo_bodega)>=6 and not tiene_espacios:  
        print(f"Producto registrado con código: {codigo_bodega}\n")
        break
    if len(codigo_bodega)<6:
        print("Código inválido. Debe tener al menos 6 caracteres.")
    if " " in codigo_bodega:
        print("Código inválido. No debe contener espacios.")