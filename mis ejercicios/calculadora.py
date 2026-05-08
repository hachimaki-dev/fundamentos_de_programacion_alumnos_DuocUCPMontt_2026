numero1 = input("Ingrese numero 1:")
numero2 = input("Ingrese numero 1:")

metodo = input("Que metodo quiere usar (suma,resta,multiplicacion,division):")
#aca me perdi y le pedi ayuda a la ia """aprendi""" sobre if,elif,int y else lo anote en el cuaderno y hice otro codigo con todo lo malo

#la ia me dijo que numero1 y 2 lo transforme en nr entero para que sea mas limpio pero cuando lo hice sin nr entero me marcaba erro no se pq
#quiero hacerlo con numero1/2 pero no me deja no se pq funciona el n1/2 y el otro no
#lo arreglue pero igual encuentro que me complique la vida

numero1 = int (numero1)
numero2 = int (numero2)



if metodo == "suma" :
    resultado  = numero1 + numero2
elif metodo == "resta" :
    resultado = numero1 - numero2
elif metodo == "multiplicacion" :
    resultado = numero1 * numero2
elif metodo == "division" :
    resultado = numero1 / numero2






print("El resultado es")
print(resultado)
