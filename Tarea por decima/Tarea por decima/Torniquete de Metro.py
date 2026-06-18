# Torniquete de Metro
# Objetivo: Cobrador automático del metro santiaguino.

# 1. Crea un ciclo while infinito hasta que el operador ingrese "CORTE".
# 2. Pide el tipo de pasajero (puede escribir: "N" para normal, "E" para estudiante, o "CORTE").
# 3. Precios: Normal $800, Estudiante $250.
# 4. Acumula el dinero total recaudado.
# 5. Y mantén contadores separados: ¿Cuántos normales pasaron? ¿Cuántos estudiantes?
# 6. Al ingresar "CORTE", el programa sale del ciclo y muestra en pantalla:
# - Pasajeros normales: X
# - Estudiantes: Y
# - Total dinero caja: Z

tipo_de_pasajero = " "
suma_pasajero_normal = 0
suma_pasajero_estudiante = 0
contador_estudiante = 0
contador_normal = 0
total = 0

print("****Cobrador de Metro****")

while True:
    tipo_de_pasajero = input("Tipo de pasajero (puede escribir: N para normal, E para estudiante, o CORTE para salir: ")
    if tipo_de_pasajero == "N":
        suma_pasajero_normal += 800
        contador_normal += 1
    elif tipo_de_pasajero == "E":
        suma_pasajero_estudiante += 250
        contador_estudiante += 1
    if tipo_de_pasajero == "CORTE":
        break
total = suma_pasajero_normal + suma_pasajero_estudiante    

print(f"Pasajeros normales: ${suma_pasajero_normal}, Cantidad: {contador_normal}")
print(f"Estudiantes: ${suma_pasajero_estudiante}, Cantidad: {contador_estudiante}")
print(f"Total dinero caja: ${total}")
pritn(f"Fin :D")