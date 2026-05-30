# Ejercicio 11 — Registro de despachos en una empresa de transporte
# Un coordinador de despachos necesita registrar los pesos de los paquetes del día. Primero ingresa cuántos paquetes despacha (entero positivo). Luego, para cada paquete:

# Ingresa el peso en kg (entero positivo, validado)
# Ingresa el código del paquete (mínimo 6 caracteres, sin espacios, validado)
# Clasifica cada paquete:

# Peso > 20 kg → Carga pesada
# Peso ≤ 20 kg → Carga normal
# Al final muestra cuántos de cada tipo y el peso total despachado.

while True:
    try:
        paquetes_despachados = int(input("Ingrese el número de paquetes a despachar: "))

        if paquetes_despachados > 0:
            break
        else:
            print("Ingrese un número entero positivo")

    except ValueError:
        print("Solo se permite números de entero positivo")

carga_normal = 0
carga_pesada = 0
carga_total = 0
total_peso_del_paquete = 0

for contador in range (1, paquetes_despachados + 1):
    while True:
        try:

            peso_del_paquete = int(input(f"Ingrese el peso de Kg del paquete N°{contador}: "))

            if peso_del_paquete > 0:
                total_peso_del_paquete += peso_del_paquete
                break
            
            print("Ingrese un número entero positivo")
        
        except ValueError:
            print("Value Error: Ingrese un número entero positivo")

    if peso_del_paquete >= 1 and peso_del_paquete <= 20:
        print("Carga normal")
        carga_normal += 1
    else:
        print("Carga pesada")
        carga_pesada += 1


    while True:
        try:
            codigo_del_paquete = input(f"Ingrese el código del paquete N°{contador}: ")

            if len(codigo_del_paquete) >= 6 and " " not in codigo_del_paquete:
                print(f"Paquete registrado: {codigo_del_paquete}")
                break
            
            print("Ingrese mínimo 6 caracteres, sin espacios.")

        except ValueError:
            print("Value Error: Ingrese un caracterer Válido")

    carga_total = carga_pesada + carga_normal

print(f"Carga Normal: {carga_normal}")
print(f"Carga Pesada: {carga_pesada}")
print(f"Carga Total: {carga_total}")
print(f"Peso Total Paquetes: {total_peso_del_paquete}")
