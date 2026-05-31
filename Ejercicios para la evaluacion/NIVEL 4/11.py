flag = True
while flag:
    try:
        cantidad_paquetes = int(input("Cuantos paquetes se despacharán? "))
        if cantidad_paquetes <= 0:
            print("Ingrese un número entero positivo de paquetes despachados.")
        else:
            print(f"La cantidad de paquetes es de {cantidad_paquetes}.")
            flag = False
    except ValueError:
        print("Ingrese números, no letras, puntos u otros caracteres especiales.")
peso_total = 0
carga_normal = 0
carga_pesada = 0
for paquetito_paqueton in range(1, cantidad_paquetes+1):
    while True:
        try:
            peso_paquete = int(input(f"Ingrese el peso del paquete n°{paquetito_paqueton}: "))
            codigo_paquete = input("Ingrese el código del paquete: ").upper()
            if len(codigo_paquete) < 6 or " " in codigo_paquete:
                print("ERROR, el codigo minimo debe tener seis caracteres y no debe tener espacios.")
                continue
            else:
                peso_total+= peso_paquete
                print(f"Peso inscrito: {peso_paquete}.\nCodigo inscrito: {codigo_paquete}.")
                break
        except ValueError:
            print("ERROR, ha ingresado mal los números del peso, recuerde que solo admitimos numeros enteros positivos.")
    if peso_paquete > 20:
        print("Carga pesada")
        carga_pesada+=1
    else:
        print("Carga normal")
        carga_normal+=1
print(f"Paquetes de carga normal: {carga_normal}.")
print(f"Paquetes de carga pesada: {carga_pesada}.")
print(f"Peso total de despacho: {peso_total}.")