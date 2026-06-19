
#1A
# while True:
#     try:
#         numero = int(input("Ingresa un número entero: "))
#         break  # Si llegó aquí, el int() funcionó → salimos del bucle
#     except ValueError:
#         print("Error: eso no es un número entero.")

# print("Número recibido:", numero)

#--------------------------------------------------------------------------------
#1B
# while True:
#     try:
#         pasajeros = int(input("ingresa numero de pasajeros: "))
#         if pasajeros > 0:
#             break
#         else:
#             print("error, ingresa un numero positivo de pasajeros")
#     except ValueError:
#         print("error, ingresa un numero positivo de pasajeros")

# print(f"vuelo registrado con {pasajeros} pasajeros")

#--------------------------------------------------------------------------------
#ejercicio 2: stock de una farmacia

# while True:
#     try:
#         medicamentos = int(input("ingresa cantidad de medicamentos: "))
#         if medicamentos > 0:
#             break
#         else:
#             print("dato invalido, ingresa un entero positivo para el stock")
#     except ValueError:
#         print("dato invalido, ingresa un entero positivo para el stock")

# print(f"stock registrado: {medicamentos} unidades disponibles")

#---------------------------------------------------------------------------------
#ejercicio 3: edad de un conductor

# print("bienvenido a la tienda de arriendo de autos")
# while True:
#     try:
#         edad = int(input("ingresa tu edad: "))
#         if edad >= 18:
#             break
#         else:
#             print("dato erroneo, ingresa una edad valida")
#     except ValueError:
#         print("dato erroneo, ingresa una edad valida")

# print(f"edad registrada: {edad} años")

#---------------------------------------------------------------------------------
#ejercicio 4: nombre de usuario

# while True:
#     try:
#         usuario = input("ingresa tu nombre de usuario: ").strip() #limpia los bordes al tener espacios
#         if len(usuario) > 6 and " " not in usuario:
#             break
#         else:
#             print("nombre invalido: debe tener minimo 6 caracteres y no contener espacios")
#     except:
#         print("nombre invalido: debe tener minimo 6 caracteres y nocontener espacios")

# print(f"usuario creado: {usuario}")

#🔀 Variación 3 — con `.replace()` para detectar espacios

# ```python
# while True:
#     nombre = input("Crea tu nombre de usuario: ")
#     sin_espacios = nombre.replace(" ", "")  # borra TODOS los espacios
#     if len(nombre) >= 6 and len(nombre) == len(sin_espacios):
#         break
#     else:
#         print("Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.")

# print("Usuario creado:", nombre)
#------------------------------------------------------------------------------
#ejercicio 5: codigo de producto en una bodega

# while True:
#     try:
#         productos = input("ingresa el codigo de producto: ").strip()
#         if len(productos) > 6 and " " not in productos:
#             break
#         else:
#             print("codigo invalido, por el codigo debe tener al menos 6 caracteres y no contener espacios")
#     except:
#         print("codigo invalido, por el codigo debe tener al menos 6 caracteres y no contener espacios")

# print(f"producto registrado con codigo: {productos}")
#-------------------------------------------------------------------------------
#ejercicio 6: patente de vehiculos en un estacionamiento

# while True:
#     patente = input("ingresa datos de tu patente: ").strip
#     try:
#         if len(patente) == 6 and " " not in patente:
#             break
#         else:
#             print("patente invalida, ingresa exactamente 6 caracteres y sin espacios")
#     except:
#         print("patente invalida, ingresa exactamente 6 caracteres y sin espacios")

# print(f"datos validos, numero de patente: {patente}")

#variacion con .upper()
# while True:
#     patente = input("Ingresa la patente del vehículo: ").strip().upper()# .upper() convierte las letras en mayusculas
#     if len(patente) == 6 and " " not in patente:
#         break
#     else:
#         print("Patente inválida. Ingresa exactamente 6 caracteres sin espacios.")

# print("Patente registrada:", patente)
#---------------------------------------------------------------------------------
#ejercico 7: clasificacion de tempetatura en una planta industrial

# tem_critica = 0
# tem_normal = 0
# tem_baja = 0
# for i in range (5):
#     temperatura = float(input(f"ingresa los datos de temperatura del sensor numero {str(i+1)}: " ))

#     if temperatura > 80:
#         print("ALERTA!! TEMPERATURA CRITICA")
#         tem_critica += 1
#     elif temperatura >= 50:
#         print("normal operativo")
#         tem_normal += 1
#     else:
#         print("temperatura baja")
#         tem_baja += 1

# print(f"temperatura criticas: {tem_critica}")
# print(f"temperatura normal: {tem_normal}")
# print(f"temperatura baja: {tem_baja}")
#-----------------------------------------------------------------------------------
#ejercicio 8: Clasificacion de ventas de un local

# ven_mayor = 0
# ven_media = 0
# ven_menor = 0
# total = 0 

# for i in range(6):
#     ventas = int(input(f"registra datos de las venta numero {str(i+1)}: "))
#     total += ventas

#     if ventas > 50000:
#         print("venta mayor")
#         ven_mayor += 1
#     elif ventas >= 10000:
#         print("venta media")
#         ven_media += 1
#     else:
#         print("venta menor")
#         ven_menor += 1

# print(f"recaudacion total: {str(total)}")
#-------------------------------------------------------------------------------------
#ejercicio 9: evaluacion de solicitud de credito

# aprobacion = 0 
# rebicion = 0
# rechazo = 0


# for i in range(8):
#     while True:
#         try:
#             solicitud = int(input(f"score del solicitante numero {str(i+1)} (de 0 a 1000): "))
#             if solicitud >= 0 and solicitud <= 1000:
#                 break
#             else:
#                 print("dato invalido, debes ingresar numeros del 0 al 1000")
#         except ValueError:
#             print("dato invalido, debes ingresar numeros enteros")
        


#     if solicitud > 750:
#         print("aprobacion automatica")
#         aprobacion += 1
#     elif solicitud >= 500:
#         print("revision manual")
#         rebicion += 1
#     else:
#         print("rechazado")
#         rechazo += 1

# print(f"solicitudes aprobadas: {aprobacion}")
# print(f"solicitudes en revision: {rebicion}")
# print(f"solicitudes rechazadas: {rechazo}")
#---------------------------------------------------------------
# ejercicio 10: registro de notas de un curso universitario
# while True:
#     try:
#         estudiantes = int(input(f"cuantos estudiantes hay?: "))
#         if estudiantes > 0:
#             break
#         else:
#             print("dato invalido, pon al menos un estudiante")
#     except: 
#         print("dato invalido, pon al menos un estudiante")


# aprobados = 0
# reprobados = 0
# suma_notas = 0

# for i in range(estudiantes):
#     while True:
#         try:
#             notas = int(input(f"nota de estudiante numero {str(i+1)}: "))
#             if notas >= 1 and notas <=7:
#                 break
#             else:
#                 print("solo son validos numeros del 1 al 7")
#         except ValueError:
#             print("ingresa numero entero")

#     suma_notas += notas

#     if notas >= 4:
#         print("aprobado")
#         aprobados += 1
#     else:
#         print("reprobado")
#         reprobados += 1

# promedio = suma_notas / estudiantes

# print("resumen")
# print(f"alumnos aprobados: {aprobados}")
# print(f"estudiantes reprobados: {reprobados}")
# print(f"promedio del curso: {promedio}")
#--------------------------------------------------------------------------------
#ejercicio 11: registro de despachos en una empresa de trasporte

# while True:
#     try:
#         despacho = int(input("ingresa cuantos despachos hay de paquetes: "))
#         if despacho > 0:
#             break
#         else:
#             print("ingresa solo numeros positivos")
#     except ValueError:
#         print("ingresa solo numeros positivos")

# carga_pesada = 0
# carga_normal = 0
# total_carga = 0

# for i in range(despacho):
#     while True:
#         try:
#             peso = int(input(f"ingresa el peso del paquete numero {str(i+1)}: "))
            
#             if peso > 0:
#                 break
#             else:
#                 print("dato invalido, solo usa numeros positivos")
#         except ValueError:
#             print("dato invalido, solo usa numeros positivos")
    
#     if peso > 20:
#         print("carga pesada")
#         carga_pesada += 1
#     else:
#         print("carga normal")
#         carga_normal += 1

        
#     while True:
#         try:
#             codigo = input(f"ingresa el codigo del paquete numero {str(i+1)}: ").strip().upper()
#             if len(codigo) >= 6 and " " not in codigo:
#                 break
#             else:
#                 print("dato invalido, ingrese solo 6 caracteres y sin espacios")
#         except ValueError:
#             print("dato invalido, ingrese solo 6 caracteres y sin espacios")

#     total_carga += peso

    

# print("resumen")
# print(f"total de cargas pesadas: {carga_pesada}")
# print(f"total de carga normal: {carga_normal}")
# print(f"total de despacho de carga: {total_carga} kg")
#----------------------------------------------------------------------------
#ejercicio 12:control de asistencia en una empresa

# while True:
#     try:
#         empleados = int(input("cuentos empleados hay en la empresa: "))
#         if empleados > 0:
#             break
#         else:
#             print("dato invalido, use solo numeros positivos")
#     except ValueError:
#         print("dato invalido, use solo numeros positivos")

# dias_completos = 0
# dias_parciales = 0

# for i in range(empleados):
#     while True:
#         try:
#             id = input(f"ingresa el id del empleado numero {str(i+1)}: ")
#             if len(id) >= 6 and " " not in id:
#                 break
#             else:
#                 print("dato invalido, ingrese solo 6 caracteres y sin espacios")
#         except ValueError:
#             print("dato invalido, ingrese solo 6 caracteres y sin espacios")

#     while True:
#         try:
#             dias = int(input("ingresa dias trabajados en el mes (0 - 23): "))
#             if dias >= 0 and dias <= 23:
#                 break
#             else:
#                 print("dato invalido, solo ingrese numeros positivos")
#         except ValueError:
#             print("dato invalido, solo ingrese numeros positivos")

#     if dias > 20:
#         print("asistencia completa")
#         dias_completos += 1
#     else:
#         print("asistencia parcial")
#         dias_parciales += 1

# print("resumen")
# print("")
# print(f"empleados con dias de trabajo completo: {dias_completos}")
# print(f"empleados con dias de trabajo parcial: {dias_parciales}")
#--------------------------------------------------------------------------------------
#ejercicio 13: inventario de computadoras en una empresa TI

# while True:
#     try:
#         computadora = int(input("cuantas computadoras hay: "))
#         if computadora > 0:
#             break
#         else:
#             print("ERROR, solo numeros positivos")
#     except ValueError:
#         print("ERROR, solo numeros positivos")

# obsoletos = 0
# vigente = 0

# for i in range(computadora):
#     while True:
#         try:
#             id_compu = input(f"ingresa el id de la computadora {str(i+1)}: ").strip().upper()
#             if len(id_compu) >= 6 and " " not in id_compu:
#                 break
#             else:
#                 print("dato invalido, ingrese solo 6 caracteres y sin espacios")
#         except ValueError:
#             print("dato invalido, ingrese solo 6 caracteres y sin espacios")
    
#     while True:
#         try:
#             año = int(input(f"ingresa el año de fabricacion {str(i+1)}: "))
#             if año >= 1990 and año <= 2026:
#                 break
#             else:
#                 print("año invalido")
#         except ValueError:
#             print("año invalido")

#     if año < 2018:
#         print("equipo obsoleto")
#         obsoletos += 1
#     else:
#         print("equipo vigente")
#         vigente += 1

# print("resumen")
# print(f"equipos obsoletos: {obsoletos}")
# print(f"equipos vigentes: {vigente}")
#------------------------------------------------------------------

#EJERCICIO 20
# stock = 60
# capacidad_maxima = 60
# historial = 0

# while True:
#     print("\n=== BIBLIOTECA TECNOLÓGICA UNIVERSIDAD DEL SUR ===")
#     print("1. Ver equipos disponibles")
#     print("2. Prestar equipo(s)")
#     print("3. Recibir devolución")
#     print("4. Ver historial de préstamos activos")
#     print("5. Salir")

#     opcion = input("Seleccione una opción: ")

#     if opcion == "1":
#         print(f"Equipos disponibles: {stock}")

#     elif opcion == "2":
#         try:
#             cantidad = int(input("Cantidad de equipos a prestar: "))

#             if cantidad <= 0:
#                 print("Error: debe ingresar un número entero positivo.")
#             elif cantidad > stock:
#                 print("Error: no hay suficientes equipos disponibles.")
#             else:
#                 stock -= cantidad
#                 historial += cantidad
#                 print(f"Préstamo realizado. Equipos disponibles: {stock}")

#         except ValueError:
#             print("Error: debe ingresar un número entero.")

#     elif opcion == "3":
#         try:
#             cantidad = int(input("Cantidad de equipos devueltos: "))

#             if cantidad <= 0:
#                 print("Error: debe ingresar un número entero positivo.")
#             elif cantidad > historial:
#                 print("Error: no se pueden devolver más equipos de los que están prestados.")
#             else:
#                 stock += cantidad
#                 historial -= cantidad
#                 print(f"Devolución registrada. Equipos disponibles: {stock}")

#         except ValueError:
#             print("Error: debe ingresar un número entero.")

#     elif opcion == "4":
#         print(f"Préstamos activos: {historial}")

#     elif opcion == "5":
#         print("Gracias por utilizar el sistema. Hasta pronto.")
#         break

#     else:
#         print("Opción no válida. Intente nuevamente.")

#------------------------------------------------------------------------
#EJERCICIO 21   

mesas_disponibles = 20
capacidad = 20
historial = 0

while True:

    print("\n=== SISTEMA DE MESAS - RESTAURANTE EL FARO ===")
    print("1. Ver mesas disponibles")
    print("2. Asignar mesa(s)")
    print("3. Liberar mesa(s)")
    print("4. Mesas ocupadas actualmente")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(f"Mesas disponibles: {mesas_disponibles}")

    elif opcion == "2":

        try:
            cantidad = int(input("¿Cuántas mesas desea asignar?: "))

            if cantidad <= 0:
                print("Error: debe ingresar un número entero positivo.")

            elif cantidad > mesas_disponibles:
                print("Error: no hay suficientes mesas disponibles.")

            else:
                mesas_disponibles -= cantidad
                historial += cantidad

                print("Mesa(s) asignada(s) correctamente.")
                print(f"Mesas disponibles: {mesas_disponibles}")

        except ValueError:
            print("Error: debe ingresar un número entero.")

    elif opcion == "3":

        try:
            cantidad = int(input("¿Cuántas mesas desea liberar?: "))

            if cantidad <= 0:
                print("Error: debe ingresar un número entero positivo.")

            elif cantidad > historial:
                print("Error: no puede liberar más mesas de las que están ocupadas.")

            else:
                mesas_disponibles += cantidad
                historial -= cantidad

                print("Mesa(s) liberada(s) correctamente.")
                print(f"Mesas disponibles: {mesas_disponibles}")

        except ValueError:
            print("Error: debe ingresar un número entero.")

    elif opcion == "4":
        print(f"Mesas ocupadas actualmente: {historial}")

    elif opcion == "5":
        print("Servicio finalizado. Buenas noches.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")

#--------------------------------------------------------------------------

# EJERCICIOS 22


# =========================
# PARTE A: REGISTRO ANIMALES
# =========================

# while True:
#     try:
#         cantidad_animales = int(input("¿Cuántos animales se registrarán?: "))

#         if cantidad_animales > 0:
#             break
#         else:
#             print("Debe ingresar un número positivo.")

#     except ValueError:
#         print("Debe ingresar un número entero.")

# grandes = 0
# pequenos = 0

# for i in range(cantidad_animales):

#     print(f"\nAnimal {i + 1}")

#     # Validar ID
#     while True:
#         animal_id = input("ID del animal: ")

#         if len(animal_id) >= 6 and " " not in animal_id:
#             break
#         else:
#             print("El ID debe tener al menos 6 caracteres y no contener espacios.")

#     # Validar peso
#     while True:
#         try:
#             peso = int(input("Peso en kg: "))

#             if peso > 0:
#                 break
#             else:
#                 print("El peso debe ser positivo.")

#         except ValueError:
#             print("Debe ingresar un número entero.")

#     # Clasificación
#     if peso > 25:
#         grandes += 1
#     else:
#         pequenos += 1

# print("\n====================================")
# print(f"La clínica ha registrado {grandes} pacientes grandes y {pequenos} pacientes pequeños.")
# print("¡Bienvenidos!")
# print("====================================")


# =========================
# PARTE B: AGENDA CLÍNICA
# =========================

# horas_disponibles = 30
# capacidad_maxima = 30
# reservas_activas = 0

# while True:

#     print("\n=== AGENDA CLÍNICA VETERINARIA PATITAS ===")
#     print("1. Ver horas disponibles")
#     print("2. Reservar hora(s)")
#     print("3. Cancelar hora(s)")
#     print("4. Ver historial de reservas")
#     print("5. Salir")

#     opcion = input("Seleccione una opción: ")

#     if opcion == "1":
#         print(f"Horas disponibles: {horas_disponibles}")

#     elif opcion == "2":

#         try:
#             cantidad = int(input("¿Cuántas horas desea reservar?: "))

#             if cantidad <= 0:
#                 print("Debe ingresar un número positivo.")

#             elif cantidad > horas_disponibles:
#                 print("No hay suficientes horas disponibles.")

#             else:
#                 horas_disponibles -= cantidad
#                 reservas_activas += cantidad

#                 print("Reserva realizada con éxito.")
#                 print(f"Horas disponibles: {horas_disponibles}")

#         except ValueError:
#             print("Debe ingresar un número entero.")

#     elif opcion == "3":

#         try:
#             cantidad = int(input("¿Cuántas horas desea cancelar?: "))

#             if cantidad <= 0:
#                 print("Debe ingresar un número positivo.")

#             elif cantidad > reservas_activas:
#                 print("No puede cancelar más horas de las reservadas.")

#             else:
#                 horas_disponibles += cantidad
#                 reservas_activas -= cantidad

#                 print("Cancelación realizada con éxito.")
#                 print(f"Horas disponibles: {horas_disponibles}")

#         except ValueError:
#             print("Debe ingresar un número entero.")

#     elif opcion == "4":
#         print(f"Reservas activas: {reservas_activas}")

#     elif opcion == "5":
#         print("Gracias por utilizar el sistema. Hasta pronto.")
#         break

#     else:
#         print("Opción no válida.")  



















