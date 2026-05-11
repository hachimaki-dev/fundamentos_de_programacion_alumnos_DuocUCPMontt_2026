codigos_respuesta_web = ["200", "404", "500", "200", "500"]
reintento_salvavidas = 1

for codigo in codigos_respuesta_web:
    if codigo == "200":
        print("OK")

    elif codigo == "404":
        print("No encontrado")
    
    elif codigo == "500" and reintento_salvavidas > 0:
        reintento_salvavidas -= 1
        print("Reintentando")
    elif codigo == "500" and reintento_salvavidas <= 0:
        print("Servidor Caido")
        break