#Desarrolla un programa en Python que gestione el registro de ingenieros recién
#incorporados al Instituto de Ingeniería Avanzada.
#El programa debe recopilar y validar los datos de cada ingeniero,
#clasificarlos según su nivel técnico y mostrar un resumen al finalizar.

ingenieros_instituto=[]
senior=0
junior=0

def pedir_registrados():
    while True:
        try:
            registrados=int(input("\n¿Cuantos ingenieros se registraran? "))
            if registrados>0:
                break
            print("Por favor ingrese un numero positivo")
        except ValueError:
            print("Error, entrada invalida")
registrados=pedir_registrados()

for r in range(registrados):
    while True:
        alias=True
        alias=input("\nPor favor ingrese su alias: ")
        if len(alias)<6:
            alias=False
            print("Tu alias debe contener al menos 6 caracteres")
        if not alias.isalnum():
            alias=False
            print("Tu alias debe contener solo caracteres alfanumericos")
        if alias:
            break
    while True:
        try:
            puntaje=int(input("Por favor ingrese su puntaje: "))
            if puntaje>0:
                if puntaje>45:
                    categoria="Senior"
                    senior+=1
                    print(f"Ingeniero {alias} registrado como {categoria} nivel {puntaje}")
                else:
                    categoria="Junior"
                    junior+=1
                    print(f"Ingeniero {alias} registrado como {categoria} nivel {puntaje}")
                break
            print("Por favor ingrese un numero positivo")
        except ValueError:
            print("Error, entrada invalida")

    ingenieros={"alias": alias, "puntaje": puntaje, "categoria": categoria}
    ingenieros_instituto.append(ingenieros)

print("\n===== Tabla de datos de nuestros ingenieros inscritos =====\n|")  
for i in ingenieros_instituto:
    print(f"|   Alias {i['alias']} | Puntaje {i['puntaje']} | Categoria {i['categoria']}")
print("|\n===========================================================\n")
print(f"¡El instituto cuenta con {senior} Ingenieros Senior y {junior} Ingenieros Junior! ¡Registro completado satisfactoriamente!\n")