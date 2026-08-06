#16. Analizador de Textos Modular Crea analizar_texto(texto) que use internamente otras funciones para contar vocales, contar palabras 
# y determinar la palabra más repetida. Debe retornar un diccionario con estos tres resultados.
diccionario_de_palabras = {
    
}
def analizar_texto(palabra):
    diccionario_de_palabras["cantidad_de_vocales"] = contar_vocales(palabra)
    diccionario_de_palabras["cantidad_de_palabras"] = contador_de_palabras(palabra)
    return diccionario_de_palabras


def contar_vocales(palabra):
    contador_de_vocales = 0
    vocales = "aeiouAEIOU"
    for letra in palabra:
        if letra in vocales:
            contador_de_vocales +=1
            print(contador_de_vocales)
    return contador_de_vocales

def contador_de_palabras(texto_ingresado):
    lista_palabras = texto_ingresado.lower().split()
    if not lista_palabras:
        return 0
    return max(lista_palabras, key=lista_palabras.count)

palabra_usuario = input("ingrsa la palabra : ")
analisis_de_palabras = analizar_texto(palabra_usuario)
print(f"el analisis de las palabras es : {analisis_de_palabras}")
    

