print("bienvenido")
print("determina tu rango de calificacion")
misiones_exitosas = int(input("ingrese su cantidad de misiones exitosas"))
daños_civiles = int(input("ingrese daños colaterales $$$"))
if misiones_exitosas == 10 and daños_civiles == 0 :
    print("HEROE CATEFORIA S, bono maximo")
elif misiones_exitosas > 5 and misiones_exitosas < 9 :
    print("heroe categoria A, cumple el promedio")
elif misiones_exitosas < 5 and daños_civiles > 10000000 :
    print("DESPEDIDO, demasiado caos")
else: 
    print("heroe en observacion")
#no entendi tanto este xd#