""" Ejercicio 12 — Control de asistencia en una empresa
Un jefe de RRHH quiere registrar la asistencia de empleados. 
Ingresa cuántos empleados tiene (entero positivo). Para cada empleado:

Ingresa su ID (mínimo 6 caracteres, sin espacios)
Ingresa los días trabajados en el mes (entero de 0 a 23, validado)
¿Por qué 0 a 23? Un empleado con licencia médica completa puede tener 
0 días trabajados. Algunos meses tienen hasta 23 días hábiles. 
El rango 0–23 cubre todos los casos reales.

Clasifica:

20 o más días → Asistencia completa
Menos de 20 días → Asistencia parcial
Muestra el resumen final. """

while True:
    try: 
        empleados = int(input("ingresa la cantidad de empleados : "))
        if empleados > 0:
            break
        else:
            print("ingresa la cantidad de empleados mayor a 0")
    except ValueError:
        print("ingresa un numero valido")

lista_empleados = []
for cantidad_de_empleados in range(len(empleados)): 
    while True:
        try:
            id_empleado = input(f"ingresa el id del empleado {cantidad_de_empleados +1 }: ")
            if len(id_empleado) >= 6 and " " not in id_empleado:
                break 
            else:
                print("ingresa el nombre minimo 6 letras y sin espacios")
        except:
            print("ingresa el nombre correctamente")
    
    
    lista_empleados.append(id_empleado)

asistencia_completa = 0
asistencia_parcial = 0

for cantidad_de_dias in range(len(lista_empleados)):
    while True:
        try:
            dias_trabajados = int(input(f"ingresa la cantidad de dias trabajados del trabajador n{cantidad_de_dias +1} : "))
            if dias_trabajados > 0 and dias_trabajados <=23:
                if dias_trabajados >= 20:
                    asistencia_completa +=1
                elif dias_trabajados < 20:
                    asistencia_parcial +=1
                break
            else:
                print("la cantidad de dias no puede ser mayor a 23 ni menor a 0 por que:\n  0 a 23? Un empleado con licencia médica completa puede tener 0 días trabajados. Algunos meses tienen hasta 23 días hábiles. El rango 0–23 cubre todos los casos reales.")
        except:
            print("ingresa un numero valido bro")

print (f" la cantidad de empleados son : {empleados}\n los id de los empleados son: {lista_empleados}\n la cantidad de trabajadores con asistencia completa son : {asistencia_completa}\n la cantidad de asistencia parcial son : {asistencia_parcial}") 
