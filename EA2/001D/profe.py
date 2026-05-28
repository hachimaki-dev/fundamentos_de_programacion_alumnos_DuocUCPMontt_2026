numero1 = 100
numero2 = int("cero")

try:
    resultado = numero1 / numero2
except TypeError:
    (print("Error de type"))
except ValueError:
    print("Error de value")
except ZeroDivisionError:
    print("Error de zero division cero")



