lista = [
    "hola", "noob", "genial", "manco"
]
for palabra in lista:
    
    if palabra in ["noob", "manco"]:
        print("[Censurado]")
        
    else:
        print(palabra)