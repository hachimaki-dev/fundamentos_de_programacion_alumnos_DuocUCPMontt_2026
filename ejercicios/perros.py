print("binvenido")
perros_paseados = int(input("cuantos perros paseo en total el dia de hoy"))
print("evaluaremos cada perro")
perros = 0
perro_pequeño  = 0
s = 2000
perro_mediano = 0
m = 4000
perro_grande = 0
l = 6000
caja = 0
while perros != perros_paseados :
    peso = int(input("ingrese peso del perro"))
    if peso < 10 :
        print("perro pequeño cuesta $2,000clp")
        perros = perros + 1
        perro_pequeño = perro_pequeño + 1
        caja = caja + s
    elif peso > 10 and peso < 25 :
        print("perro mediano cuesta $4,000clp")
        perros = perros + 1
        perro_mediano = perro_mediano + 1
        caja = caja + m
    elif peso > 25 :
        print("perro grande cuesta  $6,000clp")
        perros = perros + 1
        perro_grande = perro_grande + 1
        caja = caja + l
    else: 
        print("nosexd")

print("fin")
print(f"en total se ha ganado {caja} $$$")
print(f"has paseado {perro_pequeño} perros pequeños")
print(f"has paseado {perro_mediano} perros medianos")
print(f"has paseado {perro_grande} perros grandes")
print(f"has paseado en total {perros} perros")