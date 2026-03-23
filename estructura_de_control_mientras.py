# https://hachimaki-dev.github.io/fundamentos_de_programacion_alumnos_DuocUCPMontt_2026/
# : -> entonces
# camino True -> mientras se cumpla la condicion del while

# 1
# print("***********INICIO DEL PROGRAMA************")
# agua = 0
# while agua < 5 :
#     agua = agua + 1
#     if agua == 4 :
#         break # rompe ciclo
#     print(f"Llevamos {agua} de agua")

# print("***********FIN DEL PROGRAMA*************")

#2

# condicion = True
# while condicion:
#     print("BIENVENIDO, elija su opcion")
#     print("1. Contar chiste")
#     print("2. Contar adivinanza")
#     print("3. Salir")
#     opcion_escogida = int(input("Elejir opcion"))
#     if opcion_escogida == 1 :
#         print("chiste")
#     if opcion_escogida == 2 :
#         print("adivinanza")
#     if opcion_escogida == 3 :
#         condicion =  False
# print("******fin del programa*****")

# 3
bandera = True 
contador = 0
while bandera == True :
    print("Hola")
    contador = contador + 1
    if contador == 10 :
        print(f"Estamos a punto de salir la bandera es: {bandera}")
        bandera = False
print(f"Estamos fuera y la bandera vale: {bandera}")