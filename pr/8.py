def validar_anio(anio):
  if anio > 0 and anio <= 2026:
   return True 
  else:
    return False
  
print(validar_anio(23))
def validar_anio(anio):
   return isinstance(anio,int) and  2026 > anio > 0

print(validar_anio(200))
def validar_anio(anio):
    try:
        anio_entero = int(anio)
        return 0 < anio_entero <= 2026
        
    except (ValueError, TypeError):
        return False

#Versión con isinstance().
#Versión con try/except que intente convertir a int.