carga_pesada = 0
carga_normal = 0
total_despachado = 0
codigos_paquetes = []

while True:    
    try:
        paquetes_despacha = int(input("Ingrese Cuantos paquetes despacha :  "))
        if paquetes_despacha < 0:
            print("Ingrese una opcion valida")
            continue
        else:
            break
    except ValueError:
        print("Ingrese una opcion valida ")
        continue


for i in range(paquetes_despacha):
    print()
    while True:
        try:
            peso_del_paquete = int(input("Ingrese el peso del paquete :   "))
            if peso_del_paquete < 0 :
                print("Ingrese una opcion valida")
                continue
            else:
                total_despachado += peso_del_paquete
                break
        except ValueError:
            print("ingrese una opcion valida ")
            continue
        
    if peso_del_paquete > 20 :
        carga_pesada += 1
    elif peso_del_paquete <= 20:
        carga_normal += 1

    while True:
        codigo_del_paquete = input("Ingrese el codigo del paquete:  ")
        if len(codigo_del_paquete) < 6 or " " in codigo_del_paquete:
            print("Debe de contener el codigo al menos 6 caracteres y sin espacios")
            continue
        else:
            codigos_paquetes.append(codigo_del_paquete)
            break
    

print()
print(f"Carga Pesada : {carga_pesada}")
print(f"Carga Normal : {carga_normal}")
print(f"Lista Codigos Registrados : {codigos_paquetes}")
print(f"Total Peso Despachado : {total_despachado}")