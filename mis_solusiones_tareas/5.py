
while True:
    codigo = input("inrese el nomre del codigo")

    if len(codigo) >6 and " " not in codigo :
        print(f"produsto regitrado con codigo : {codigo}")
    break
else:
     print("error: no se pudo inresar el codigo por favor , deve tener minimo 6 caraster sin espasio ")
