def contar_vocales(texto):
    contador = 0
    vocales_jiji = 'aeiouAEIOU'
    for p in texto:
        if p in vocales_jiji:
            contador += 1
    return contador

def contar_palabras(texto):
    lista_palabras = texto.split()
    return len(lista_palabras)

def palabra_repetida(texto):
    lista_palabras = texto.split()
    if not lista_palabras:
        return "ninguno"
    return max(lista_palabras, key=lista_palabras.count)

def analizar_texto(texto):
    total_vocales = contar_vocales(texto)
    total_palabras = contar_palabras(texto)
    mas_repetida = palabra_repetida(texto)
    resultado_final = {"cantidad vocales" : total_vocales,
                       "total palabras"   : total_palabras,
                    "palabra mas repetida": mas_repetida}
    return resultado_final
variable_para_calcular = input("ingresa una palabra: ")
diccionario_resultado = analizar_texto(texto=variable_para_calcular)
print(diccionario_resultado)