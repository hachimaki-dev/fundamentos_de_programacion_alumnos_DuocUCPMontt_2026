""" Ejercicio 18 — Sistema de registro de técnicos en una empresa minera
Una empresa minera necesita registrar a sus técnicos de mantención. 
El sistema debe:

Preguntar cuántos técnicos se registrarán (entero positivo, 
validado con mensaje de error)

Para cada técnico pedir:
Código de técnico: mínimo 6 caracteres, sin espacios (validado)
Años de experiencia: entero positivo (validado con mensaje de error)
Clasificar según experiencia:
Más de 10 años → Técnico Maestro
10 años o menos → Técnico Operario
Llevar conteo de cada categoría

Al finalizar mostrar:
"La planta cuenta con 4 Técnicos Maestros y 6 Técnicos Operarios. 
Sistema listo." """
while True:
    try:
        registro_de_tecnicos = int(input("cuantos tecnicos ingresaran? : "))
        if registro_de_tecnicos > 0:
            break
        else:
            print("ingresa un numero mayor que 0")
    except ValueError:
        print("ingresa un numero valido")
    

codigos_de_tecnicos = []
for cada_codigo_tecnico in range(registro_de_tecnicos):
    while True:
        try:
            codigo_de_tecnico = input(f"ingresa el codigo del tecnico {cada_codigo_tecnico +1} : ")
            if len(codigo_de_tecnico) >=6 and " " not in codigo_de_tecnico:
                break
            else:
                print("los parametros para ingresar son: minimo 6 letras y sin espacios")
        except :
            print("ingresa bien los datos solicitados")
    codigos_de_tecnicos.append(codigo_de_tecnico) 


tecnico_maestro = 0
tecnico_operario = 0

for anos_de_experiencia in range(len(codigos_de_tecnicos)):
    while True:
        try:
            ano_de_experiencia = int(input(f"ingresa los anos de exp del tecnico {anos_de_experiencia + 1} : "))
            if ano_de_experiencia > 0:
                if ano_de_experiencia > 10:
                    tecnico_maestro +=1
                    break
                elif ano_de_experiencia <=10:
                    tecnico_operario +=1
                    break
            else:
                print("ingresa un numero mayor que 0")

        except ValueError:
            print("ingresa un numero valido")

print(f" La planta cuenta con:\n {tecnico_maestro} Técnico\s Maestro\s\n {tecnico_operario} Técnico\s Operario\s.\n Sistema listo.\n")