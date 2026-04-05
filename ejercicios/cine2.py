print("bienvenido")
entradas = int(input("cuantas entradas van a comprar en total"))
entrada = 0
niño = 3000
adulto = 6000
adulto_mayor = 4000
caja = 0
while entrada != entradas :
    edad = int(input("ingrese la edad de la persona"))
    if edad < 12 :
        print("el valor de la entrada es 3,000clp")
        caja = caja + niño
        entrada = entrada + 1
    elif edad > 11 and edad < 64 :
        print("el valor de la entrada es 6,000clp")
        caja = caja + adulto
        entrada = entrada + 1
    elif edad >= 65 :
        print("el valor de su entrada es 4,000clp")
        caja = caja + adulto_mayor
        entrada = entrada + 1
    
print(f"el valor final por todas las entradas es {caja}")
print("fin")