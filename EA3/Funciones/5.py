def contar_vocales(text: str) -> int:
    counter = 0
    for character in text:
        if character.lower() in ["a", "e", "i", "o", "u"]:
            counter += 1

    return counter

print(contar_vocales("Buenos dias, ¿como estas?"))