#Ejercicio 11 — Registro de despachos en una empresa de transporte
#Un coordinador de despachos necesita registrar los pesos de los paquetes del día. Primero ingresa cuántos paquetes despacha (entero positivo). Luego, para cada paquete:

#Ingresa el peso en kg (entero positivo, validado)
#Ingresa el código del paquete (mínimo 6 caracteres, sin espacios, validado)
#Clasifica cada paquete:

#Peso > 20 kg → Carga pesada
#Peso ≤ 20 kg → Carga normal
#Al final muestra cuántos de cada tipo y el peso total despachado.

while True:
    try:
        paquetes = int(input("Ingresa la cantidad de paquetes: "))
        if paquetes > 0:
            break
        else:
            print("Error: ingresa un número entero mayor a 0")
    except ValueError:
        print("Error: ingresa un número valido")

pesado = 0
normal = 0
peso_total = 0

for i in range(paquetes):
    
    while True:
        try:
            peso = int(input(f"Ingresa el peso del paquete {i + 1} en kg: ")).strip()
            if peso > 0:
                break
            else:
                print("Error: ingresa un número entero mayor a 0")
        except ValueError:
            print("Error: ingresa un número valido")
    
    while True:
            codigo = input(f"Ingresa el códido del paquete {i + 1 }: ").strip()
            if len(codigo) >= 6 and " " not in codigo:
                break
            print("Error: tu código debe tener al menos 6 carácteres y sin espacios")

    peso_total += peso

    if peso > 20:
        pesado += 1
        print("Carga pesada")
    else:
        normal += 1
        print("Carga normal")

print("\n---------------------------------------------------")
print(f"Carga pesada = {pesado}")
print(f"Carga normal = {normal}")
print(f"Total de kg = {peso_total} kg")
print("---------------------------------------------------")