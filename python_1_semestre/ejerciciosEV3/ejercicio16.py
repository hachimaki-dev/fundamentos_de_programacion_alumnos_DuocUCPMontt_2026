""" Ejercicio 16 — Gestión de turnos en un servicio de urgencias
Un hospital gestiona los turnos de atención en urgencias. Comienza con 0 pacientes en sala. Capacidad máxima: 25 pacientes.

=== URGENCIAS HOSPITAL REGIONAL ===
1. Ver pacientes en sala
2. Registrar ingreso de paciente(s)
3. Registrar alta de paciente(s)
4. Total de ingresos del turno
5. Salir
Reglas:

No puede haber más pacientes que la capacidad máxima
No se puede dar de alta más pacientes de los que hay
El historial de ingresos aumenta con cada ingreso y disminuye con cada alta (igual que en la evaluación)"""


sala = 0 
turnos = []
registro_de_paciente = 0
alta_pasiente = 0
ingresos = 0

while True:
    try:
        menu = int(input("=== URGENCIAS HOSPITAL REGIONAL ===\n 1. Ver pacientes en sala\n 2. Registrar ingreso de paciente\n 3. Registrar alta de paciente(s)\n 4. Total de ingresos del turno\n 5. Salir"))
        
        if menu == 1:
            
            print(f"la cantidad de pasientes en sala es: {sala}")
        
        
        elif menu == 2:
            registro_de_paciente = int(input("ingresa el paciente(s) a la sala MAXIMO 25 : "))
            
            if registro_de_paciente > 25 :
                print("la cantidad maxima de pacientes en sala son 25")
            
            elif (registro_de_paciente <= 25 and registro_de_paciente > 0) and sala + registro_de_paciente <= 25:
                sala += registro_de_paciente
                ingresos += registro_de_paciente
            
            else:
                print("ingresa un numero valido que no sea mayor que la capacidad de la sala (25)")
        

        elif menu == 3:
            alta_pasiente = int(input("ingrese la alta del pasiente(s)"))
            
            
            if alta_pasiente > sala:
                print("el numero ingresado de alta no puede ser mayor que la cantidad de pacientes en sala")
            
            elif alta_pasiente < 0:
                print("ingresa un numero mayor a 0")
            
            else:
                sala -= alta_pasiente
                ingresos -= alta_pasiente
        
        elif menu ==4:
            print(f"total ingresos del turno {ingresos}")
        
        elif menu == 5:
            break
        
        else :
            print("ingresa un numero valido del menu del 1 al 4")

            

    
    except ValueError:
        print("ingresa un numero entero")