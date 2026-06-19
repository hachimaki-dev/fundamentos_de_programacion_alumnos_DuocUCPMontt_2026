def buscar_alumno(rut, diccionario_alumno):
    for nombre, rut_alumno in diccionario_alumno.items():
        if rut_alumno == rut:
            return nombre
    return "no encontrado"
diccionario_clase = {
    'miguel': '22.333.111-0',
    'andrea': '18.444.555-k',
    'diego': '20.111.222-3'
}
print(buscar_alumno('22.333.111-0', diccionario_clase))