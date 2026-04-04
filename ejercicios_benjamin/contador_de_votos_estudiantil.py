# preguntar la cantidad de estudiantes 
n = int(input("¿cuantos estudiantes votaran?")) 

# contadores 
a_favor = 0 
en_contra = 0 

# ciclo para contar los votos
i = 0
while i < n: 
    voto = input("ingrese su voto (a favor/en contra): ")

    if voto == "a favor":
        a_favor += 1
    elif voto == "en contra":
        en_contra += 1
    else:
        print("voto en nulo, voto no contabilizado")
    i += 1

    #comparar resultados 
print("\nResultados:")
print("a favor:", a_favor)
print("en contra:", en_contra)

if a_favor > en_contra:
    print("Gana a favor")
elif en_contra > a_favor:
    print("Gana en contra")
else:
    print("Empate")     