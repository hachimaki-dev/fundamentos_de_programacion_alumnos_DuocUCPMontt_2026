#INPUTS PARTE 3 
#INPUTS SITUACIONALES COMO QUE PASA SI EL USARIO ESCRIBE HOLA ENVEZ DE UN NUMERO ? 
#PYTHON LANZA UN ERRROR (value error) . se puede manejar con try/except. 
print(("=" * 20),"INGRESO DE NUMERO SEGURO", ("=" * 20))

try: 
    numero = int(input("ingresa un numero entero: "))
    print(f"ingresaste el numero: {numero} ")
except ValueError:
    print("¡Error! Eso no es un número entero válido.")