#INICIO
numero_encuestados = 0
contadorA = 0
contadorC = 0
VotoA = "A"
VotoC = "C"
eleccion_estudiante = ""
votos_nulos = 0

print("Votación de estudiantes")
print("*Importante* para votar por favor ingresar A = (A favor) o bien C = (En contra)")
numero_encuestados = int(input("¿Cuantos estudiantes seran encuestados?: "))

while votos_nulos < numero_encuestados :
    eleccion_estudiante = input("Eliga A o C : ")
    if eleccion_estudiante == VotoA :
        contadorA += 1
    elif eleccion_estudiante == VotoC :
        contadorC += 1
    else:
        print("Voto no contabilizado")
    votos_nulos += 1

if contadorA > contadorC :
    print(f"Gano A Favor con {contadorA} votos")
if contadorC > contadorA :
    print(f"Gano En Contra con {contadorC} votos")
if contadorC == contadorA :
    print("Empate")
#FIN DE LA ENCUESTA
        
   





