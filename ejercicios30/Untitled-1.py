contador_a = 0 
frase_vocal = input("Escribe un texto: ").lower()
lista_vocales = "a"
for caracter in frase_vocal:
     if caracter.lower() in lista_vocales.lower() == "a":
       contador_a += 1
     print(f"El texto tiene {contador_a}letras a ")

print()
