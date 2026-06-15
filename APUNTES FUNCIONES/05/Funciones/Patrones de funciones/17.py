def crear_estudiante(nombre, edad, nota):
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "nota": nota,
        "aprobado": False  # siempre inicia en False, no se pide al usuario
    }
    return estudiante