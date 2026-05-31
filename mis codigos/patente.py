
while True:
    try:
            patente = input("escribe tu patente")
            contador = 0
            for i in patente:
              if i == " ":
               raise ValueError
              contador = contador + 1
            if contador < 6:
                raise ValueError
            print(f"la patente es {patente}")
            break
    except ValueError:
        print("minimo 6 caraterez y sin espacios")