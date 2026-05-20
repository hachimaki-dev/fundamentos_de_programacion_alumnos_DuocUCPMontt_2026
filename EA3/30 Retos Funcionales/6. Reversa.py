#Crea reversar_texto(texto) que devuelva el string al revés. (Ej: "hola" -> "aloh")

def reverso_texto(texto):
    resultado = ""

    for letra in texto:
        resultado = letra + resultado
    return resultado

print(reverso_texto("Hola"))