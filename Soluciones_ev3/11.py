while True:
    try:
        paquetes = int(input("Ingrese la cantidad de paquetes: "))
        if paquetes > 0:
            break
        else:
            print("ERROR, debe ser un numero positivo")
    except ValueError:
        print("ERROR, SOLO numeros enteros positivos")
    

carga_pesada = 0
carga_normal = 0
peso_total = 0

for i in range(paquetes):
    print(f"Datos del Paquete {i + 1}")
    while True:
        try:
            peso = int(input("Ingrese el peso del paquete (en Kg): "))
            if peso > 0:
                break
            else:
                print("ERROR, el peso debe ser un numero positivo")
        except ValueError:
            print("El peso debe ser un numero entero positivo")
    
    while True:
            codigo = input("Ingrese el codigo del paquete (min 6 caracteres, sin espacios): ")
            if len(codigo) >= 6 and " " not in codigo:
                break
            else:
                print("ERROR, el codigo debe tener min 6 caracteres y sin espacios")
    peso_total += peso
    if peso > 20:
        print("Carga pesada")
        carga_pesada += 1
    else:
        print("Carga normal")
        carga_normal += 1

print(f"Paquetes de Carga Pesada: {carga_pesada}")
print(f"Paquetes de Carga Normal: {carga_normal}")
print(f"Peso Total: {peso_total}")