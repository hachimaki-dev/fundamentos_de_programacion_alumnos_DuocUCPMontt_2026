#Crea analizar_texto(texto) que use internamente otras funciones para contar vocales, contar palabras y determinar la palabra más repetida. Debe retornar un diccionario con estos tres resultados.
def contar_vocales(texto):
    contadorvocales = 0
    vocales = ['a','A','e','E','i','I','o','O','u','U']
    for i in texto:
        if i in vocales:
            contadorvocales +=1 
    return contadorvocales
def contar_palabras(texto):
    contadorpalabras = 0
    palabras = texto.split()
    return len(palabras)
def frecuencia_palabras(texto):
    texto = texto.upper()
    palabras = texto.split()
    resultado = {}
    for i in palabras:
        if i not in resultado:    
            resultado[i]= 1
        elif i in resultado:
            resultado[i]+=1  
    return resultado        
def analizar_texto(texto):
    vocales = contar_vocales(texto)
    cantidad_palabras= contar_palabras(texto)
    frecuencia = frecuencia_palabras(texto)
    analisis = {
        "Vocales en el texto" : vocales,
        "Cantidad de palabras" : cantidad_palabras,
        "Frecuencia de palabras" : frecuencia
    }

    return analisis

print (analizar_texto("The quick brown fox jumps over the lazy dog, but also the fox has a machine gun lmao. The dog doesn't care"))

