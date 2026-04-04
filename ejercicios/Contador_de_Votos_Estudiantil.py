n_encuestados = int(input("¿cuantos estudiantes van a votar?"))
contador_a = 0 
contador_c = 0 
contador_encuestado = 0 
while contador_encuestado < n_encuestados :
    contador_encuestado += 1 
    voto = input(f"estudiante {contador_encuestado} ingrese su voto (A para a favor / C para encontra)")
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
