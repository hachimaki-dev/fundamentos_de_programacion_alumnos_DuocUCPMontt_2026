#Acumulador de plata 
total_dinero = 0

#contadores 
normales = 0
estudiantes = 0


#ciclo de while infinito
while True:
    tipo = input("ingrese el tipo de pasajero (N/E) o 'CORTE' para finalizar: ")

   #condicion de corte 
    if tipo == "CORTE":
        break 
   #precios y conteos
    elif tipo == "N":
        total_dinero += 500
        normales += 1
    elif tipo == "E":
        total_dinero += 250
        estudiantes += 1
    else:
        print("Tipo de pasajero no válido. Intente nuevamente.")
        continue
#resultados finales 
print("\n--- CIERRE DE CAJAS ---") 
print(f"pasajeros normales: {normales}") 
print(f"pasajeros estudiantes: {estudiantes}") 
print(f"total de dinero caja: ${total_dinero}") 

    