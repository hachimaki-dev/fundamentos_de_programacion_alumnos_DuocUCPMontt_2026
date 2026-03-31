corte = "*"
edad_minima = float("inf")
nombre = input(f"Ingrese un nombre , {corte} para cortar :")
while nombre != corte:
    edad = int(input(f"Ingrese su edad de {nombre} : "))
    if edad < edad_minima:
        edad_minima = edad
        nombre_mas_joven = nombre
    nombre = input(f"ingrese otro nombre {corte} para cortar :")
print(f"La persona mas joven es ({edad_minima} años) {nombre_mas_joven}  ")    
