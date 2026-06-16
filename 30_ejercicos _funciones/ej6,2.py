def reversa_texto(texto):
    texto = "".join(reversed(texto))
    return texto
resultado = reversa_texto(input("ingresa una palabra o texto: "))
print(resultado)