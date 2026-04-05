# Torniquete de Metro
# Objetivo: Cobrador automático del metro santiaguino.

# 1. Crea un ciclo while infinito hasta que el operador ingrese "CORTE".
# 2. Pide el tipo de pasajero (puede escribir: "N" para normal, "E" para estudiante, o "CORTE").
# 3. Precios: Normal $800, Estudiante $250.
# 4. Acumula el dinero total recaudado.
# 5. Y mantén contadores separados: ¿Cuántos normales pasaron? ¿Cuántos estudiantes?
# 6. Al ingresar "CORTE", el programa sale del ciclo y muestra en pantalla:
#     - Pasajeros normales: X
#     - Estudiantes: Y
#     - Total dinero caja: Z

print(" TORNIQUETE DE METRO ".center(50,"-"))

cantidad_normales = 0
cantidad_estudiantes = 0
valor_pasaje = 0
total_recaudado = 0
tipo_pasajero = ""

while True:
    tipo_pasajero = input("\nIngrese el tipo de pasajero\n'N' normal | 'E' estudiante | 'CORTE' para finalizar\nIngrese el tipo de pasajero: ").upper()
    
    if tipo_pasajero == "CORTE":
        print("\nDetalle:")
        print(f"-Pasajeros normales: {cantidad_normales} \n-Estudiantes: {cantidad_estudiantes} \n-Total dinero caja: ${total_recaudado}")
        break
    elif tipo_pasajero == "N":
        cantidad_normales += 1
        valor_pasaje = 800
    elif tipo_pasajero == "E":
        cantidad_estudiantes +=1
        valor_pasaje = 250
    else:
        print("\n*****Opcion invalida, intente nuevamente****")
        valor_pasaje = 0
        continue

    total_recaudado = total_recaudado + valor_pasaje

    