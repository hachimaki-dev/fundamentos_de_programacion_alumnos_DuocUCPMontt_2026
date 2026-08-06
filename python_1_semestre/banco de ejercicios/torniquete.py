""" Objetivo: Cobrador automático del metro santiaguino.

1. Crea un ciclo while infinito hasta que el operador ingrese "CORTE".

2. Pide el tipo de pasajero (puede escribir: "N" para normal, "E"
 para estudiante, o "CORTE").

3. Precios: Normal $800, Estudiante $250.

4. Acumula el dinero total recaudado.

5. Y mantén contadores separados: ¿Cuántos normales pasaron? ¿Cuántos estudiantes?

6. Al ingresar "CORTE", el programa sale del ciclo y muestra en pantalla:
- Pasajeros normales: X
- Estudiantes: Y
- Total dinero caja: Z"""


contador_normal = 0
contador_estudiante = 0
tipo_de_pago = 0
dinero_total = 0


while tipo_de_pago != "CORTE":
    tipo_de_pago = input(" n para normla, e para estudiante o CORTE")
    print("precios: normal: $800 , estudiante: $250")
    
    if tipo_de_pago == "e":
        pago = int(input("ingrese el pago: "))
        contador_estudiante = contador_estudiante + 1
        dinero_total = dinero_total + pago
        
    elif tipo_de_pago == "n":
        pago = int(input("ingrese el pago: "))
        contador_normal = contador_normal + 1
        dinero_total = dinero_total + pago
    

print(f"personas normales: {contador_normal} , estudiantes: {contador_estudiante}, total caja {dinero_total}")