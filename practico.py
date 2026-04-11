import time
valor_2d = 5500
valor_2d_estudiante = 2500
valor_3d = 8000
contador = 0
contador_monetario = 0
print("--Cine--")
print("Estos son los valores de las entradas al cine , marque como opcion valida por numero")
print(f"1.2D = ${valor_2d}")
print(f"2. 2D ESTUDIANTES = ${valor_2d_estudiante}")
print(f"3. 3D = ${valor_3d}")
opcion_escogida = int(input("Ingrese su opcion"))
print("Esperando al servidor..")
time.sleep (5)
while True : 
    if opcion_escogida == 1 :
        print(f"Ha escogido el valor de 2D , el valor de su entrada es ${valor_2d}")
        time.sleep(5)
        print("desea mas entradas?")
        entradas = input("Si o No : ").lower
        if entradas == "si":
            contador_monetario = valor_2d + valor_2d
            contador = contador + 1 + 1
            print(f"Su cantidad de entradas es : {contador}")
            print(f"Valor total a pagar : {contador_monetario}")
            break
        elif entradas == "no":
            print(f"su valor a pagar es {valor_2d}")
    if opcion_escogida == 2:
        print(f"Ha escogido el valor de 2D ESTUDIANTE , el valor de su entrada es ${valor_2d_estudiante} ")
        print("desea mas entradas?")
        time.sleep(5)
        entradas = input("Si o No : ").lower
        if entradas == "si":
            contador_monetario = valor_2d_estudiante + valor_2d_estudiante
            contador = contador + 1 + 1
            print(f"Su cantidad de entradas es : {contador}")
            print(f"Valor total a pagar : {contador_monetario}")
            break
        elif entradas == "no":
            print(f"su valor a pagar es {valor_2d_estudiante}")
            break
    if opcion_escogida == 3 :
         print(f"Ha escogido el valor de 3D, el valor de su entrada es ${valor_2d_estudiante} ")
         print("desea mas entradas?")
         time.sleep(5)
         entradas = input("Si o No : ").lower
         if entradas == "si":
            contador_monetario = valor_2d_estudiante + valor_2d_estudiante
            contador = contador + 1 + 1
            print(f"Su cantidad de entradas es : {contador}")
            print(f"Valor total a pagar : {contador_monetario}")
            break
         elif entradas == "no":
            print(f"su valor a pagar es {valor_2d_estudiante}")
            break