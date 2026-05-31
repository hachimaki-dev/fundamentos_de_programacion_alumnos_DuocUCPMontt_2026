numero1 = int(input("Ingrese primer numero :"))
numero2 = int(input("Ingrese segundo numero :"))

try:
    resultado = numero1 / numero2
    print(f"El resultado es { resultado }")
    
except ValueError:
    print(" No se puede divivir por cero VALUERROR")
except ZeroDivisionError:
    print("No se puede dividir por cero ZeroDivisionError")
    