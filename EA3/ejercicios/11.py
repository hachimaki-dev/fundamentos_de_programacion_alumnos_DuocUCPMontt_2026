#Crea contar_caracteres(texto) que retorne un diccionario donde las claves son las letras y los valores son la cantidad de veces que aparecen.
def contar_caracteres(texto):
    
    resultado = {}
    for i in texto:
        if i not in resultado:    
            resultado[i]= 1
        elif i in resultado:
            resultado[i]+=1    
            
    return resultado

print (contar_caracteres("hola a todos"))    