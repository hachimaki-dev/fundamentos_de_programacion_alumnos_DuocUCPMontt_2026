"""
Objetivo: Cobrador automático del metro santiaguino.

1. Crea un ciclo while infinito hasta que el operador ingrese "CORTE".
2. Pide el tipo de pasajero (puede escribir: "N" para normal, "E" para estudiante, o "CORTE").
3. Precios: Normal $800, Estudiante $250.
4. Acumula el dinero total recaudado.
5. Y mantén contadores separados: ¿Cuántos normales pasaron? ¿Cuántos estudiantes?
6. Al ingresar "CORTE", el programa sale del ciclo y muestra en pantalla:
- Pasajeros normales: X
- Estudiantes: Y
- Total dinero caja: Z
"""
tipo_pasajero = ""
dinero_total = 0
normales = 0
estudiantes = 0
print("Bienvenido al Cobrador automático del metro santiaguino")
print("Recuerde:")
print("N para normal, $800")
print("E para estudiante, $250")
print("CORTE para salir")
while tipo_pasajero != "CORTE":
    tipo_pasajero = input("Cual es el tipo de pasajero?")
    if tipo_pasajero == "N":
        normales = normales + 1
        dinero_total = dinero_total = 800
        print(f"Llevas {normales} normales")
    elif tipo_pasajero == "E":
        estudiantes = estudiantes + 1
        dinero_total = dinero_total + 250
        print(f"Llevas {estudiantes} estudiantes")
    elif tipo_pasajero != "CORTE":
        print()
        print()
        print("No valido")
print(f"- Pasajeros normales: {normales}")
print(f"- Estudiantes: {estudiantes}")
print(f"- Total dinero caja: {dinero_total}")