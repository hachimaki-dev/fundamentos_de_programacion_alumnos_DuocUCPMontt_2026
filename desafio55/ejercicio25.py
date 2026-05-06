insultos = ["Hola", "Genial!", "Noob", "Manco", "Maricarmen", "Bobo", "Bobolon", "Webong"]

for palabra in insultos:
    if palabra in ["Noob", "Manco", "Maricarmen", "Bobo", "Bobolon", "Webong"]:
        print("CENSURADO")
    else:
        print(palabra)