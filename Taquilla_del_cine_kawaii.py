cantidad_de_entradas_a_comprar= int(input("¿Cuántas entradas desea comprar?: "))
total_entradas=0
entradas=1

while entradas<= cantidad_de_entradas_a_comprar:
    edad= int(input("Ingrese su edad: "))
    if edad<12:
        total_entradas+=3000
        entradas+=1
    elif 12<=edad<=64:
        total_entradas+=6000
        entradas+=1
    elif edad>=65:
        total_entradas+=4000
        entradas+=1

print(f"El total a pagar por las entradas es de: ${total_entradas}")