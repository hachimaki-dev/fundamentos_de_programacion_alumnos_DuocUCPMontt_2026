total_a_pagar=0
cantidad_de_productos=0
precio= -1

while precio !=0:
    precio=float(input("ingrese el precio del productos(0 para finalizar):"))
    if precio !=0:
        total_a_pagar += precio
        cantidad_de_productos +=1
    if cantidad_de_productos>=3:
        total_a_pagar=total_a_pagar*0.9
    print(f"total a pagar : ${total_a_pagar}")
    print(f"cantidad de producto:{cantidad_de_productos}")
    