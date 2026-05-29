#Error de Valor: ValueError
#int(input("Ingrese un valor")) = Solicita un valor en especifico.

#Error división por cero: ZeroDivisionError
#print(número/0)

#o también

#num1 = int(input("Ingrese primer número: "))
#num2 = int(input("Ingrese segundo número: "))



#~~~~Solución~~~~

#while True:
#   try:
#       num1 = int(input("Ingrese primer número: "))
#       num2 = int(input("Ingrese segundo número: "))

#       resultao = num1 / num2
#       break

#   except ValueError:
#       print("Ha ocrrido un error, se esperaba un número entero")
#   except ZeroDivisionError:
#       print("Oye compadre, no puedes divir por 0, intenta con otro número")

# cuando no tienes un error argumentado, no va a entrar como error y se terminara el codigo con normalidad.
#   except:
#       print("Wena")



#password = input("Crea tu password")

#if len(password) < 8:
#   print("La password debe tener al menos 8 caracteres")
#else:
#   print("Password valida")



#palabra = "esta palabra tiene espacios"

#contador_espacios = 0
#for cada_letra == " ":
#    contador_espacios += 1

#print(contador_espacios)