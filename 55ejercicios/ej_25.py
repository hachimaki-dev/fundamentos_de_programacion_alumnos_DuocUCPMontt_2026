# Ejercicio 25: Filtro de Palabras (Discord)

print("=============================")
print("Sistema de moderación de chat")
print("=============================")

mensajes = ['hola', 'noob', 'genial', 'manco']

for palabra in mensajes:

    if palabra in ['noob', 'manco']:
        print("[CENSURADO]")

    else:
        print(palabra)