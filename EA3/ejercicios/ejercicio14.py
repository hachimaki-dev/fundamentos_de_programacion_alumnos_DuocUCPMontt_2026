#Crea buscar_alumno(rut, diccionario_alumnos) que retorne el nombre del alumno si el rut existe, o "No encontrado" si no.
diccionario_alumnos_1d= {
 '20.123.123-4' : 'Pepito',
  '19.123.123-4' : 'Jose', 
  }

def buscar_alumno(rut_b, diccionario_alumnos):
    if str(rut_b) in diccionario_alumnos:
        return diccionario_alumnos[rut_b]
    else:
        return ("No encontrado")
    
print (buscar_alumno('20.123.123-4', diccionario_alumnos_1d))   
    

    #WIP