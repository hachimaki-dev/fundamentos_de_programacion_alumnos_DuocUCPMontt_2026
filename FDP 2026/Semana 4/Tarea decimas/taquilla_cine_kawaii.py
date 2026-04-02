cantidad_entradas = int(input("Ingresa la cantidad de entradas a comprar: "))
total = 0
contador = 0
edad_user = 0

while contador < cantidad_entradas:
    edad_user = int(input(f"¿Cual es la edad de la persona {contador + 1}?: "))
    
    if edad_user < 12:
        total += 3000
    elif edad_user >= 12 and edad_user <= 64:
        total += 6000
    else:
        total += 4000

    contador += 1

print(f"Total a pagar: ${total}")