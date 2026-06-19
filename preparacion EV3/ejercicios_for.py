#ejercicio 1: formulario de validacion
# while True:
#     try:
#         edad = int(input("Ingresa tu edad: "))
#         if edad > 0:
#             break
#         else:
#             print("Entrada inválida. Ingresa un número entero positivo.")
#     except ValueError:
#         print("Entrada inválida. Ingresa un número entero positivo.")

# print(f"Edad registrada: {edad} años.")


#-----------------------------------------------------------------------------
#ejercicio 2: clasificacion y contadores

# while True:
#     try:
#         cantidad = int(input("¿Cuántos alumnos? "))
#         if cantidad > 0:
#             break
#         print("Ingresa un número mayor a 0.")
#     except ValueError:
#         print("Entrada inválida.")

# aprobados = 0
# reprobados = 0

# for i in range(cantidad):
#     while True:
#         try:
#             nota = int(input(f"Nota alumno {i+1}: "))
#             if 1 <= nota <= 100:
#                 break
#             print("La nota debe estar entre 1 y 100.")
#         except ValueError:
#             print("Ingresa una nota entera válida.")
            
#     if nota > 59:
#         print("→ Aprobado")
#         aprobados += 1
#     else:
#         print("→ Reprobado")
#         reprobados += 1

# print(f"Resultado: {aprobados} aprobados y {reprobados} reprobados.")
#-----------------------------------------------------------------------------
#ejercicio 3: sistema de registros de atletas

# while True:
#     try:
#         cantidad = int(input("cuantos atletas habran: "))
#         if cantidad > 0:
#             break
#         else:
#             print("invalido, solo usa numeros enteros positivos")
#     except ValueError:
#         print("invalido, solo usa numeros enteros positivos")

# elite = 0
# regular = 0

# for i in range(cantidad):
#     print(f" atleta numero {i+1}")
#     while True:
#         try:
#             codigo = input(f"ingresa el codigo del atleta numero {i+1}: ")
#             if len(codigo) >= 5 and " " not in codigo:
#                 break
#             else:
#                 print("codigo invalido, tiene que haber al menos 5 caracteres")
#         except ValueError:
#             print("codigo invalido, tiene que haber al menos 5 caracteres")
    
#     while True:
#         try:
#             puntaje = int(input(f"que puntaje ha rendido el atleta numero {i+1}: "))
#             if puntaje > 0:
#                 break
#             else:
#                 print("error, solo usa numeros positivos")
#         except ValueError:
#             print("error, solo usa numeros positivos")

#     if puntaje > 70:
#         print("atleta de elite")
#         elite += 1
#     else:
#         print("atleta regular")
#         regular += 1

# print(f"hay {elite} atletas con rendimiento de elite")

# print(f"hay {regular} atletas con rendimiento regular")
#------------------------------------------------------------------------------------
#ejercicio 4: menu interactivo (calculadora)

# numero = 0

# while True:
#     print("\n=== CALCULADORA ===")
#     print("1. Sumar número al total")
#     print("2. Ver total acumulado")
#     print("3. Reiniciar total")
#     print("4. Salir")

#     opcion = int(input("que operacion quieres realizar: "))

#     if opcion == 1:
#         while True:
#             try:
#                 suma = int(input("ingresa un numero entero: "))
#                 numero += suma
#                 break
#             except ValueError:
#                 print("error, debe ser un numero entero")
#     elif opcion == 2:
#         print(f"este es tu total actual: {numero}")
#     elif opcion == 3:
#         numero = 0
#         print("reinicio")
#     elif opcion == 4:
#         print("hasta luego")
#         break
#     else:
#         print("opcion invalida, solo use las opciones disponibles")

#------------------------------------------------------------------------------------
#ejercicio 5: sistema de gestion de biblioteca
# disponibles = 30
# capacidad = 30
# historial_neto = 0

# print("¡Bienvenido al sistema de préstamos de la Biblioteca Central!")
# while True:
#     print("\n=== MENÚ PRINCIPAL ===")
#     print("1. Libros disponibles")
#     print("2. Registrar préstamo")
#     print("3. Registrar devolución")
#     print("4. Movimientos de la sesión")
#     print("5. Salir")
    
#     op = input("Elige una opción: ")
    
#     if op == "1":
#         print(f"Libros disponibles actualmente: {disponibles}")
#     elif op == "2":
#         while True:
#             try:
#                 prestamo = int(input("Cantidad de libros a prestar: "))
#                 if prestamo <= 0:
#                     print("Ingresa un número positivo.")
#                 elif prestamo > disponibles:
#                     print(f"No hay suficientes libros. Solo quedan {disponibles} disponibles.")
#                     break
#                 else:
#                     disponibles -= prestamo
#                     historial_neto += prestamo
#                     print("Préstamo registrado exitosamente.")
#                     break
#             except ValueError:
#                 print("Ingresa un número entero válido.")
#     elif op == "3":
#         while True:
#             try:
#                 devolucion = int(input("Cantidad de libros a devolver: "))
#                 if devolucion <= 0:
#                     print("Ingresa un número positivo.")
#                 elif disponibles + devolucion > capacidad:
#                     print(f"Operación inválida. Superaría el límite máximo de {capacidad} libros.")
#                     break
#                 else:
#                     disponibles += devolucion
#                     historial_neto -= devolucion
#                     print("Devolución registrada exitosamente.")
#                     break
#             except ValueError:
#                 print("Ingresa un número entero válido.")
#     elif op == "4":
#         print(f"Historial neto de la sesión (Préstamos - Devoluciones): {historial_neto}")
#     elif op == "5":
#         print("Gracias por usar el sistema de la biblioteca. ¡Hasta pronto!")
#         break
#     else:
#         print("Opción no válida. Elige entre 1 y 5.")

#------------------------------------------------------------------------------------
#ejercicio 6: sistema de gestion de estacionamiento

# espacios_disponibles = 20

# capacidad = 20

# jornada_neta = 0

# while True:
#     print("\n=== PANEL DE CONTROL ===")
#     print("1. Espacios disponibles")
#     print("2. Registrar entrada de vehículo")
#     print("3. Registrar salida de vehículo")
#     print("4. Resumen de la jornada")
#     print("5. Salir")
    
#     op = input("Selecciona una opción (1-5): ")
    
#     if op == "1":
#         print(f"Espacios libres actuales: {espacios_disponibles}")
#     elif op == "2":
#         while True:
#             try:
#                 entradas = int(input("Vehículos que ingresan: "))
#                 if entradas <= 0:
#                     print("Debe ser mayor a 0.")
#                 elif entradas > espacios_disponibles:
#                     print(f"No hay suficientes espacios. Solo quedan {espacios_disponibles} lugares.")
#                     break
#                 else:
#                     espacios_disponibles -= entradas
#                     jornada_neta += entradas
#                     print(f"Registro exitoso. Entraron {entradas} vehículos.")
#                     break
#             except ValueError:
#                 print("Ingresa un entero válido.")
#     elif op == "3":
#         while True:
#             try:
#                 salidas = int(input("Vehículos que salen: "))
#                 if salidas <= 0:
#                     print("Debe ser mayor a 0.")
#                 elif espacios_disponibles + salidas > capacidad:
#                     print("Operación inválida. Se superaría la capacidad máxima del estacionamiento.")
#                     break
#                 else:
#                     espacios_disponibles += salidas
#                     jornada_neta -= salidas
#                     print(f"Registro exitoso. Salieron {salidas} vehículos.")
#                     break
#             except ValueError:
#                 print("Ingresa un entero válido.")
#     elif op == "4":
#         print(f"Balance neto de vehículos ingresados hoy: {jornada_neta}")
#     elif op == "5":
#         print("Cerrando sistema. ¡Hasta mañana!")
#         break
#     else:
#         print("Opción no reconocida. Selecciona del 1 al 5.")
#------------------------------------------------------------------------------------
#ejercicio 7: estructura de datos (listas y diccionarios)

# pacientes = []

# for i in range(3):
#     while True:
#         try:
#             nombre = input("nombre de paciente: ").strip()
#             if len(nombre) > 0:
#                 break
#             else:
#                 print("el nombre no puede estar vacio")
#         except ValueError:
#             print("el nombre no puede estar vacio")
#     while True:
#         try:
#             edad = int(input("edad del paciente: "))
#             if edad > 0:
#                 break
#             else:
#                 print("numero invalido, ingresa numero mayor a 0")
#         except ValueError:
#             print("numero invalido, ingresa numero entero")

#     paciente = {
#         "nombre": nombre,
#         "edad": edad
#     }
#     pacientes.append(paciente)


# for p in pacientes:
#     print(f" nombre: {p['nombre']} | edad: {p['edad']}")

#-------------------------------------------------------------------------
#ejercicio 8: inventario dinamico de productos

while True:
    try:
        cantidad = int(input("¿Cuántos productos registrar? "))
        if cantidad > 0:
            break
        print("Ingresa un entero positivo.")
    except ValueError:
        print("Ingresa un entero válido.")

inventario = []

for i in range(cantidad):
    print(f"\n--- Producto {i+1} ---")
    while True:
        try:
            nombre = input("Nombre del producto: ").strip()
            if len(nombre) >= 3 and " " not in nombre:
                break
            print("Nombre inválido. Mínimo 3 caracteres y sin espacios (usa una sola palabra).")
            
        except ValueError:
            print("Nombre inválido. Mínimo 3 caracteres y sin espacios (usa una sola palabra).")
    while True:
        try:
            precio = int(input("Precio: "))
            if precio > 0:
                break
            print("El precio debe ser un número positivo.")
        except ValueError:
            print("Ingresa un número entero válido.")
            
    producto = {"nombre": nombre, "precio": precio}
    inventario.append(producto)

print("\n--- Inventario ---")
for p in inventario:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']}")
#-------------------------------------------------------------------------
#ejercicio 9: registro y clasificacion de voluntario

while True:
    try:
        cantidad = int(input("¿Cuántos voluntarios registrar? "))
        if cantidad > 0:
            break
        print("Debe ser mayor a 0.")
    except ValueError:
        print("Ingresa un número entero válido.")

voluntarios = []
dedicados = 0
casuales = 0

for i in range(cantidad):
    print(f"\n--- Voluntario {i+1} ---")
    while True:
        nombre = input("Nombre clave: ").strip()
        if len(nombre) >= 4 and " " not in nombre and nombre.isalnum():
            break
        print("Código inválido. Mínimo 4 caracteres, sin espacios y alfanumérico.")
        
    while True:
        try:
            horas = int(input("Horas disponibles por semana: "))
            if horas > 0:
                break
            print("Las horas deben ser mayor a 0.")
        except ValueError:
            print("Ingresa un número entero válido.")
            
    if horas > 20:
        categoria = "Voluntario Dedicado"
        dedicados += 1
    else:
        categoria = "Voluntario Casual"
        casuales += 1
        
    vol = {
        "nombre": nombre, 
        "horas": horas, 
        "categoria": categoria}
    voluntarios.append(vol)

print(f"\nLa ONG tiene {dedicados} Voluntarios Dedicados y {casuales} Voluntarios Casuales. ¡Gracias por su apoyo!")

#------------------------------------------------------------------------
#ejercicio 10: busqueda en una lista de diccionario

pacientes = [
    {"nombre": "Ana", "edad": 34},
    {"nombre": "Luis", "edad": 28},
    {"nombre": "María", "edad": 45}
]

busqueda = input("¿Qué nombre deseas buscar?: ").strip()
encontrado = False

for p in pacientes:
    if p["nombre"].lower() == busqueda.lower():
        print(f"Paciente encontrado → Nombre: {p['nombre']} | Edad: {p['edad']}")
        encontrado = True
        break

if not encontrado:
    print("Paciente no encontrado.")

#--------------------------------------------------------------------------
#ejercicio 11: filtrar y promediar desde una lista




while True:
    try:
        cantidad = int(input("¿Cuántos miembros quiere registrar? "))
        if cantidad > 0:
            break
        print("Ingresa un entero positivo.")
    except ValueError:
        print("Ingresa un entero válido.")

miembros = []
for i in range(cantidad):
    print(f"\n--- Miembro {i+1} ---")
    while True:
        nombre = input("Nombre clave: ").strip()
        if len(nombre) > 0:
            break
        print("El nombre no puede estar vacío.")
        
    while True:
        try:
            meses = int(input("Meses de membresía: "))
            if meses > 0:
                break
            print("Los meses deben ser mayor a 0.")
        except ValueError:
            print("Ingresa un entero válido.")
            
    miembros.append({"nombre": nombre, "meses": meses})

print("\n--- Todos los Miembros ---")
suma_meses = 0
for m in miembros:
    print(f"Nombre: {m['nombre']} | Membresía: {m['meses']} meses")
    suma_meses += m["meses"]

print("\n--- Miembros frecuentes (más de 6 meses) ---")
for m in miembros:
    if m["meses"] > 6:
        print(f"Nombre: {m['nombre']} | Membresía: {m['meses']} meses")

promedio = suma_meses / len(miembros) if len(miembros) > 0 else 0
print(f"\nPromedio de membresía: {promedio:.2f} meses")

#----------------------------------------------------------------------------
#ejercicio 12: modificar y eliminar(CRUD) en listas

productos = [
    {"nombre": "Arroz", "stock": 50},
    {"nombre": "Aceite", "stock": 20},
    {"nombre": "Harina", "stock": 35}
]

while True:
    print("\n=== GESTIÓN DE PRODUCTOS ===")
    print("1. Ver todos los productos")
    print("2. Actualizar stock de un producto")
    print("3. Eliminar un producto")
    print("4. Salir")
    
    op = input("Opción: ")
    
    if op == "1":
        print("\n--- Productos en Stock ---")
        for p in productos:
            print(f"Producto: {p['nombre']} | Stock: {p['stock']}")
            
    elif op == "2":
        buscar = input("Nombre del producto a actualizar: ").strip()
        encontrado = False
        for i, p in enumerate(productos):
            if p["nombre"].lower() == buscar.lower():
                while True:
                    try:
                        nuevo_stock = int(input(f"Nuevo stock para {p['nombre']}: "))
                        if nuevo_stock >= 0:
                            productos[i]["stock"] = nuevo_stock
                            print("Stock actualizado exitosamente.")
                            encontrado = True
                            break
                        print("El stock debe ser 0 o superior.")
                    except ValueError:
                        print("Ingresa un entero válido.")
                break
        if not encontrado:
            print("Producto no encontrado.")
            
    elif op == "3":
        buscar = input("Nombre del producto a eliminar: ").strip()
        encontrado = False
        for i, p in enumerate(productos):
            if p["nombre"].lower() == buscar.lower():
                eliminado = productos.pop(i)
                print(f"Producto {eliminado['nombre']} eliminado exitosamente.")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")
            
    elif op == "4":
        print("Saliendo del panel de gestión.")
        break
    else:
        print("Opción no reconocida. Selecciona del 1 al 4.")






