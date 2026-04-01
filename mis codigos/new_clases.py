n = int(input("Ingres el numero de los encuestados: "))
todos_votaron = False
a_favor = 0
en_contra = 0
contador = 1

while contador <= n :
    voto = int(input("1. A favor, 2. En contra"))
    if voto == 1:
        a_favor = a_favor + 1
        contador = contador + 1
    elif voto == 2:
        en_contra = en_contra + 1
        contador = contador + 1
    else:
        print("Por favor elija entre 1 a favor o 2 en contra")
