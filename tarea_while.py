numero_para_adivinar = 7 
intento = 0

while intento < 7:
    intento = int(input("coloca tu número:"))
    if intento ==7:
        print("adivinaste!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    elif intento < 7:
        print("muy bajo")
    else:
        print("muy alto")
