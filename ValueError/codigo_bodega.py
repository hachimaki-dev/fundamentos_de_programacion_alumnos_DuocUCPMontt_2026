# Código de producto en una bodega
# Una bodega industrial registra productos por código. El código debe:

# Tener al menos 6 caracteres
# No tener espacios
# Pide el código hasta que sea válido. Luego muestra:

# "Producto registrado con código: PROD7X"
# Ejercicio de análisis: ¿Qué función de Python usarías para detectar si hay espacios? Hay al menos dos formas distintas. Encuentra ambas.
codigos_de_bodega = []

try :
    codigo_ingresado = str(input("Ingrese el codigo ")).upper()
    if len(codigo_ingresado) >= 6 and " " not in codigo_ingresado:
        codigos_de_bodega.append(codigo_ingresado)
        print(f"Codigo guardado en lista {codigos_de_bodega}")
    else :
        print("Debe tener mas de 6 caracteres y sin espacios ")
except Exception as error_valor_ingresado :
    print(f"Se ha producido un error en el valor ingresado : {error_valor_ingresado}")