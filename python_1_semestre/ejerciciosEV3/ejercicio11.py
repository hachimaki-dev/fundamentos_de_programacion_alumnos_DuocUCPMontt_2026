""" Ejercicio 11 — Registro de despachos en una empresa de transporte

Un coordinador de despachos necesita registrar los pesos de los paquetes del día.
 Primero ingresa cuántos paquetes despacha (entero positivo). 
 Luego, para cada paquete:

Ingresa el peso en kg (entero positivo, validado) # validar significa que tengo 
que hacer que sea un numero realista como mayor a 0
Ingresa el código del paquete (mínimo 6 caracteres, sin espacios, validado)
Clasifica cada paquete:

Peso > 20 kg → Carga pesada
Peso ≤ 20 kg → Carga normal
Al final muestra cuántos de cada tipo y el peso total despachado. """

pesos= []
while True:
    try:
        paquetes = int(input("ingresa la cantidad de envios : "))
        if paquetes > 0:
            break
        else:
            print("ingresa la cantidad de paquetes mayor a 0 ")
    except:
        print("ingresa un numero real de paquetes ")

carga_pesada = 0
carga_normal = 0
total_peso = 0

for cantidad_de_pesos in range(paquetes):
    while True:
        try:
            pesos_por_paquete = float(input(f"ingresa el peso del paquete {cantidad_de_pesos +1} : "))
            total_peso += pesos_por_paquete
            if pesos_por_paquete >0:
                break
            else:
                print("ingresa un peso real de paquete")
        except:
            print("ingresa un peso en numeros validos")
    pesos.append(pesos_por_paquete)
    
    if pesos_por_paquete > 20:
        carga_pesada +=1
    elif pesos_por_paquete <= 20:
        carga_normal +=1

codigos = []
for codigo_por_unidad in range(paquetes):
    while True:
        try:
            codigo = input("ingresa el codigo de cada paquete ")
            if len(codigo) >= 6 and " " not in codigo:
                break 
            else:
                print("ingresa el codigo de barras correctamente sin espacios y mayor que 6 caracters")
        except:
            print("ingresa el codigo de barras bien ")
    
    codigos.append(codigo)
    tamano_de_codigos = len(codigo)
    print(f"{codigos}")

print(f" total carga pesada: {carga_pesada}\n total carga normal: {carga_normal}\n total peso : {total_peso}kg")    




