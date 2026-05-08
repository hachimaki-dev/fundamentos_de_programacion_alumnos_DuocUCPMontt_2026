mensajes = ["hola", "noob", "genial", "Manco"]
palabras_sancionadas = ["noob", "Manco"]

for mensaje in mensajes:
    if mensaje in palabras_sancionadas:
        print("[CENSURADO]", end="\\n")
    else:
        print(mensaje, end="\\n")
 
print()