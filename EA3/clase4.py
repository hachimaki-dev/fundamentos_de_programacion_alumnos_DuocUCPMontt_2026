from random import randint

limite_inferior = int(input("Ingresar el limite inferior"))
limite_superior = int(input("Ingresar el limite superior"))
numero_aleatorio_generado = randint(limite_inferior, limite_superior)
intento_1_guardado = 0
intento_2_guardado = 0

contador_de_intentos = 0

if numero_aleatorio_generado % 2 != 0:
  #Es impar
  if numero_aleatorio_generado == limite_superior:
    numero_aleatorio_generado -= 1
  elif numero_aleatorio_generado != limite_superior:
    numero_aleatorio_generado += 1

for contador_de_intentos_for in range(1,4):
  intento_del_usuario = int(input("Intente adivinar"))
  if intento_del_usuario == numero_aleatorio_generado:
    print("Adivinaste, eres el mejor <3 tqm")
    break
  elif intento_del_usuario != numero_aleatorio_generado:
    print("Fallaste")
    if contador_de_intentos == 0:
      contador_de_intentos += 1
      intento_1_guardado = intento_del_usuario
      if intento_1_guardado < numero_aleatorio_generado:
        print("El numero aleatorio geneado es mayor que el intento")
      else:
        print("El numero aleatorio geneado es menor que el intento")
    elif contador_de_intentos == 1:
      contador_de_intentos += 1
      intento_2_guardado = intento_del_usuario
      if intento_2_guardado < numero_aleatorio_generado:
        print("El numero aleatorio geneado es mayor que el intento")
        if abs(numero_aleatorio_generado - intento_1_guardado ) < abs(numero_aleatorio_generado - intento_2_guardado):
          print("El intento 1 esta mas cerca del numero aleatorio generado")
          print(f"EL intento 1 es {intento_1_guardado}")
          print(f"EL intento 2 es {intento_2_guardado}")
        else:
          print("El intento 2 esta mas cerca del numero aleatorio generado")
          print(f"EL intento 1 es {intento_1_guardado}")
          print(f"EL intento 2 es {intento_2_guardado}")
      else:
        print("El numero aleatorio geneado es menor que el intento")
        if abs(numero_aleatorio_generado - intento_1_guardado ) < abs(numero_aleatorio_generado - intento_2_guardado):
          print("El intento 1 esta mas cerca del numero aleatorio generado")
          print(f"EL intento 1 es {intento_1_guardado}")
          print(f"EL intento 2 es {intento_2_guardado}")
        else:
          print("El intento 2 esta mas cerca del numero aleatorio generado")
          print(f"EL intento 1 es {intento_1_guardado}")
          print(f"EL intento 2 es {intento_2_guardado}")

    elif contador_de_intentos == 2:
      print(f"Fallaste el numero a adivinar era { numero_aleatorio_generado}")
      break
