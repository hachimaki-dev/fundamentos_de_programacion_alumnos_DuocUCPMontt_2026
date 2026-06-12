opcion = leer_opcion()

if opcion == 1:
    agregar_estudiante(lista)
elif opcion == 2:
    buscar_estudiante(lista)
elif opcion == 3:
    eliminar_estudiante(lista)
elif opcion == 6:
    print("Adiós")
    break

acciones = {
    1: opcion_agregar,
    2: opcion_buscar,
}

opcion = 1
if opcion in acciones:
    acciones[opcion]()  # se ejecuta con los paréntesis
else:
    print("Opción inválida")