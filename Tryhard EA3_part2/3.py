#Contexto: El Centro Deportivo Nacional necesita registrar atletas de nueva incorporación.
#Lo que debe hacer el programa: Pregunta cuántos atletas registrar (si escribe letras o un número negativo, vuelve a preguntar). Por cada atleta:
#1) Pide un código (debe tener al menos 5 caracteres, sin espacios, solo letras y números — si no cumple, repregunta).
#2) Pide su puntaje de rendimiento (entero positivo).
#3) Si el puntaje es mayor a 70 → muestra "Atleta Élite". Si es 70 o menor → muestra "Atleta Regular".
#Al final muestra cuántos de cada tipo hay.


while True:
    try:
        atletas_registrados=int(input("\n¿Cuantos atletas se registraran? "))
        if atletas_registrados>0:
            break
        print("Dato invalido. Por favor ingrese un numero positivo")
    except ValueError:
        print("Entrada invalida.")

elite=0
regular=0

for i in range(atletas_registrados):
    print(f"\nAtleta N{i+1} ")
    while True:
        codigo=input("Por favor ingrese un codigo de al menos 5 caracteres. ")
        if len(codigo)>=5 and " " not in codigo and codigo.isalnum():
            break
        print("Código inválido. Debe tener al menos 5 caracteres, sin espacios y solo letras o números.")

    while True:
        try:
            puntaje=int(input("Por favor ingrese su puntaje: "))
            if puntaje >0:
                break
        except ValueError:
            print("Entrada invalida.")
        print("Dato invalido. Por favor ingrese un numero positivo")
    if puntaje>70:
        elite+=1
        print("Atleta Élite")
    else:
        regular+=1
        print("Atleta Regular")
print(f"Hay {elite} atletas élite y {regular} atletas regulares.\n")