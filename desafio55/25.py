#Ejercicio 25: Filtro de Palabras (Discord)
#Crea un robot moderador de chat que censure insultos.

#Datos Iniciales: Tienes una lista de mensajes en el chat: `['hola', 'noob', 'genial', 'manco']`.

#Reglas de Negocio: El bot revisa las palabras una por una. Las palabras 'noob' y 'manco' 
# están prohibidas. Si el bot ve una de esas palabras, debe cambiarla por el texto '[CENSURADO]'. Si la palabra es buena, la deja igual.

#Restricciones: Recorre la lista con un `for`. Adentro, usa un `if` para revisar 
# si la palabra es mala e imprimir la censura, sino, imprime la palabra original.

#Pista de Ayuda:
#Usa if palabra in ['noob', 'manco'] dentro del for.
#Resultado esperado en consola:
#hola\n[CENSURADO]\ngenial\n[CENSURADO]



mensajes_sucios  = ['hola', 'noob', 'genial', 'manco']
contador = 0


for i in mensajes_sucios:
   if i == "noob" or i == "manco":
    mensajes_sucios [contador]  = "censurado"
    contador = contador + 1

    
print(mensajes_sucios)