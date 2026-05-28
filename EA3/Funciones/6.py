def reversar_texto(text: str) -> str:
    reversed = ""

    for i in range(len(text)):
        reversed += text[- i - 1]

    return reversed

print(reversar_texto("I've brought peace, freedom, justice and security to my new empire"))