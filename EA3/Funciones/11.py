def contar_caracteres(text: str) -> dict:
    dictionary = {}

    for character in text.lower():
        if character not in dictionary.keys():
            dictionary[character] = 1
        else:
            dictionary[character] += 1

    return dictionary

print(contar_caracteres("Your new empire?"))
print(contar_caracteres("Anakin, my allegiance is to the republic, to democracy!"))