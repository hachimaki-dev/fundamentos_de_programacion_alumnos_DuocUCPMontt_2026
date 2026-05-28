while True:
    try:
        edad_condustor = int(input("inresa tu edad para poder arendar un auto"))
    
        if edad_condustor >18 :
            print(f"edad regitrada : {edad_condustor} años ")
            break
        elif edad_condustor >0:
            print("eres menor no puedes arrendar un auto")
        else:
            print("error: no puedes tener una edad negativa")
    except ValueError:
        print("este no es un numero inresa un numero por favor")
  