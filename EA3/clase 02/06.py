#Crea reversar_texto(texto) que devuelva el string al revés. (Ej: "hola" -> "aloh")

def reversar_texto(texto):
    texto_invertido = ""
    for letra in texto:
        #IMPORTANTE: el texto invertido debe ir despues de cada letra recorrida si se realiza el += te escribirá todo de nuevo :P
        texto_invertido = letra + texto_invertido 
    return texto_invertido
    
reverso = reversar_texto("Ana lava la tina")
print(reverso)
