n_encuestados = int(input("¿cuantos estudiantes van a votar?"))
contador_a = 0 
contador_c = 0 
i= 0 
while i < n_encuestados :
    i += 1 
    voto = input(f"estudiante {i} ingrese se voto (A para a favor / C para encontra)")
    if voto == "A" or voto == "a":
        contador_a += 1 
    elif voto == "C" or voto == "c":
        contador_c += 1 
    else:
        print("voto nulo no contabilizado")
        i += 1 
if contador_a  > contador_c:
    print("Gano A favor")
elif contador_c > contador_a:
    print("Gano encontra")
if contador_a == contador_c:
    print("Empate")
