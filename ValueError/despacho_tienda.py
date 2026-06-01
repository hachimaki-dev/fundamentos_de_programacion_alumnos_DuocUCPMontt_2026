#Ejercicio 11 — Registro de despachos en una empresa de transporte
#Un coordinador de despachos necesita registrar los pesos de los paquetes del día. Primero ingresa cuántos paquetes despacha (entero positivo). Luego, para cada paquete:

#Ingresa el peso en kg (entero positivo, validado)
#Ingresa el código del paquete (mínimo 6 caracteres, sin espacios, validado)
#Clasifica cada paquete:

#Peso > 20 kg → Carga pesada
#Peso ≤ 20 kg → Carga normal
#Al final muestra cuántos de cada tipo y el peso total despachado.
paquetes_ingresados = {
    "carga_normal": 0,
    "carga_pesada": 0
}
peso_total = 0

while True:
    try:
        cantidad_paquetes = int(input("Ingrese cuántos paquetes despacha hoy: "))
        if cantidad_paquetes <= 0:
            print("Debe ser un número positivo")
            continue
        else:
            for paquetes in range(cantidad_paquetes):
                peso_ingresado = int(input("Ingrese el peso del paquete \n"))
                codigo_paquete = str(input("Ingrese el codigo del paquete \n"))
                if peso_ingresado <= 0:
                    print("Peso invalido. Debe ser positivo")
                    continue
                if len(codigo_paquete) < 6 or " " in codigo_paquete:
                    print("Codigo invalido")
                    continue
                if len(codigo_paquete) >= 6 and " " not in codigo_paquete:
                    print(f"Codigo de producto : {codigo_paquete} ingresado correctamente")
                    if peso_ingresado > 20:
                        print("Carga pesada")
                        paquetes_ingresados["carga_pesada"] += 1
                    elif peso_ingresado <= 20:
                        print("Carga normal")
                        paquetes_ingresados["carga_normal"] += 1
                peso_total += peso_ingresado
            print(f"Resumen\n {paquetes_ingresados}" )
            print(f"Peso total\n {peso_total}")
            break
    except Exception as e:
        print(f"Error: {e}")