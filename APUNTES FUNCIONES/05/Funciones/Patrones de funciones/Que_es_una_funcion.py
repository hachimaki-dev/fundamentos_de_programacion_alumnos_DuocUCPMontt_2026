def lavarse_dientes():
    print("Agarrar cepillo")
    print("Cepillar 2 minutos")
lavarse_dientes()  # invocación
lavarse_dientes()  # se puede usar cuantas veces quieras

def lavarse_dientess(minutos):  # "minutos" es PARÁMETRO
    print(f"Cepillando por {minutos} minutos")
lavarse_dientess(2)  # "2" es el ARGUMENTO