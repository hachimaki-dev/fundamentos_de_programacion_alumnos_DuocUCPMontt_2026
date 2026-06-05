diccionario_alumnos_1d= {
 '20.123.123-5' : 'Pepito',
  '19.123.123-5' : 'Jose', 
  }
def buscar_alumno(rut_b, diccionario_alumno):
    if str(rut_b) in diccionario_alumno:
        return diccionario_alumno[rut_b]
    else:
        return("No encontrado")
print(buscar_alumno('20.123.123-5',diccionario_alumnos_1d))