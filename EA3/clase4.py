from random import randint

limite_inferior = int(input("Ingrese limite inferior"))
limite_superior = int(input("Ingrese limite superior"))

numero_aleatorio_generado = randint(limite_inferior, limite_superior)

intento_1_guardado = 0
intento_2_guardado = 0
contador_de_intentos = 0


#Preguntar si el numero generado es impar

if numero_aleatorio_generado % 2 != 0:
  if numero_aleatorio_generado == limite_superior:
    numero_aleatorio_generado -= 1

  else:
    numero_aleatorio_generado += 1



for numero_de_intento in range(1,4):
  adivinando_intento = int(input("Intente adivinar"))
  
  if adivinando_intento == numero_aleatorio_generado:
    print("Felicidades, ganaste eres el mas mejor <3")
    break

  elif adivinando_intento != numero_aleatorio_generado:

    if contador_de_intentos == 0:
      print("INCORRECTO")
      contador_de_intentos += 1
      intento_1_guardado = adivinando_intento
      
      if intento_1_guardado < numero_aleatorio_generado:
        print("EL numero aleatorio generado es mayor")

      else:
        print("EL numero aleatorio generado es menor")

        

    elif contador_de_intentos == 1:
      intento_2_guardado = adivinando_intento

      if intento_2_guardado < numero_aleatorio_generado:
        print("INCORRECTO")
        print("EL numero aleatorio generado es mayor")

        if abs(numero_aleatorio_generado - intento_1_guardado) < (numero_aleatorio_generado - intento_2_guardado):
          print(f"El primer intento esta mas cerca del numero aleatorio generado")
          print(f"Intento 1 {intento_1_guardado}")
          print(f"Intento 2 {intento_2_guardado}")

        else:
          print(f"El segundo intento esta mas cerca del numero aleatorio generado")
          print(f"Intento 1 {intento_1_guardado}")
          print(f"Intento 2 {intento_2_guardado}")

      else:
        print("EL numero aleatorio generado es menor")
        
        if abs(numero_aleatorio_generado - intento_1_guardado) < (numero_aleatorio_generado - intento_2_guardado):
          print(f"El primer intento esta mas cerca del numero aleatorio generado")
          print(f"Intento 1 {intento_1_guardado}")
          print(f"Intento 2 {intento_2_guardado}")

        else:
          print(f"El segundo intento esta mas cerca del numero aleatorio generado")
          print(f"Intento 1 {intento_1_guardado}")
          print(f"Intento 2 {intento_2_guardado}")



    elif contador_de_intentos == 2:
      print(f"Fallaste el número a adivinar era {numero_aleatorio_generado}")
      break