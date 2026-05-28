import string

def contar_vocales(text: str) -> int:
    counter = 0
    for character in text:
        if character.lower() in ["a", "e", "i", "o", "u"]:
            counter += 1

    return counter

def contar_palabras(text: str) -> int:
    return len(text.split(" "))

def palabra_mas_repetida(text: str) -> str | None:
    if len(text) == 0:
        return None
    
    punctuation_symbols = string.punctuation
    clean_text = text.lower()

    for symbol in punctuation_symbols:
        clean_text = clean_text.replace(symbol, "")

    words = clean_text.split()

    if len(words) == 1:
        return words[0]

    frecuencies = {}

    for word in words:
        if word in frecuencies:
            frecuencies[word] += 1
        else:
            frecuencies[word] = 1

    winner_word = None
    max_repeated = 0

    for word, count in frecuencies.items():
        if count > max_repeated:
            max_repeated = count
            winner_word = word

    if max_repeated == 1:
        return "No hubo palabra más repetida"
    else:
        return winner_word

def analizar_texto(text: str) -> dict:
    analysis = {"vocales": 0, "palabras": 0, "mas_repetida": ""}

    analysis["vocales"] = contar_vocales(text)
    analysis["palabras"] = contar_palabras(text)
    analysis["mas_repetida"] = palabra_mas_repetida(text)

    return analysis

print(palabra_mas_repetida("hola como estas, Hola, estoy probando esta funcion hola hola"))