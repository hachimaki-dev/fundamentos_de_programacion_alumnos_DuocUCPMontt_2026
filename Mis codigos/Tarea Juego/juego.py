
palabras_correctas = ["PYTHON", "CODIGO", "LOGICA", "BUCLE", "LISTA", "VARIABLE", "CADENA", "ENTERO", "FUNCION", "CONSOLA", "OBJETO", "RECURSO", "PROCESO", "TECLADO", "PANTALLA"]
palabras_desordenadas = ["YPHTNO", "GIDOCO", "CIALGO", "ELUBC", "STILA", "BAVALRIE", "NEDACA", "REETNO", "COINFUN", "OLSACON", "TEJOBO", "SRUOCRE", "SCEOPRO", "DALOTEC", "TALLAPAN"]

print("Bienvenido al juego")
print("Instrucciones: ")

nombre_jugador = input("Ingrese su nombre: ")
palabra_elegida = ""
palabra_correcta = ""
intentos = 5

while True:
    eleccion = int(input("Ingrese un numero del 1 al 15: "))
    palabra_elegida = palabras_desordenadas[eleccion-1]
    palabra_correcta = palabras_correctas[eleccion-1]
    print(f"Ordena la palabra: {palabra_elegida}")
    print(palabra_correcta)
    while intentos > 0:
        if palabra_elegida == palabra_correcta:
            print("ganaste")
            break
            

    break

