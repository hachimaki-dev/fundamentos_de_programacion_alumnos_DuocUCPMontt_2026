hoppers = "hoppers"
FNAF_2 = "FNAF_2"
mario_galaxy = "mario galaxy"
son_como_niños2 = "son como niños 2"
película = ""
numero_entradas = 0
numero_consultas = numero_entradas
#personas_por_consultar = numero_personas - numero_consultas
adultos_jovenes = 6000
#6000
menores12 = 3000
#3000
viejos = 4000
#4000
total_valor = 0


print("BIENVENIDO AL CINE")
peli = input("¿Que película va a ver? ")
numero_entradas = int(input("¿Cuántas entradas va a comprar?"))
numero_entradasB = numero_entradas
while numero_entradas > 0:
   for personas in [numero_entradas]:
        personas = int(input (f"ingrese edad de la {numero_entradas}° entrada"))
        if personas > 12 and personas < 65:
            total_valor = adultos_jovenes + total_valor
        elif personas < 12:
            total_valor = menores12 + total_valor
        else:
            total_valor = viejos + total_valor

        numero_entradas = numero_entradas - 1



print(f"Excelente, {numero_entradasB} para la película: {peli}, serían {total_valor} pesos")


    
