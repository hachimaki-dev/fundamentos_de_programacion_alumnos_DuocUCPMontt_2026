#Crea buscar_alumno(rut, diccionario_alumnos) que retorne el nombre del alumno si el rut existe, o "No encontrado" si no.

def buscar_alumno(rut, diccionario_alumnos):
    if rut in diccionario_alumnos:
        return diccionario_alumnos[rut]
    else:
        return "No encontrado"

alumnos = {
   '20121265-0':'Zobeiba',
   '21755451-3':'Karte'
}
alumno = buscar_alumno('11524451-k', alumnos)
print(alumno)