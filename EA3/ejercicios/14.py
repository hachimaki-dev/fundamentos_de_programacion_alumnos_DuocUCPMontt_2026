#Crea buscar_alumno(rut, diccionario_alumnos) que retorne el nombre del alumno si el rut existe, o "No encontrado" si no.
diccionario_alumnos_1d= [
{'rut' : '20.123.123-4', 
 'nombre' : 'Pepito'}, 
{'rut' : '19.123.123-4', 
 'nombre' : 'Jose'}
]
def buscar_alumno(rut, diccionario_alumnos):
    if rut in diccionario_alumnos:
        return diccionario_alumnos('nombre')
    
print (buscar_alumno('20.123.123-4', diccionario_alumnos_1d))   
    

    #WIP