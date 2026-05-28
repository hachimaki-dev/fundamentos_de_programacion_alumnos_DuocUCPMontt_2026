#tarea inplementar esta caculadora con
#menu de ociones 1 sumo . 2 resto . 3 multiplica . 4 divide , 5 sale , cualquiera otro numero es invalido . los numero deve ser input




def sumar(numero_1 , numero_2):
    return numero_1 + numero_2

def multiplicar(numero_1 , numero_2):
    return numero_1 * numero_2

def restar(numero_1 , numero_2):
    return numero_1 - numero_2

def division(numero_1 , numero_2):
    return numero_1 // numero_2

def solisitar_dos_numeros():
    numero_1 = int(input("inresa numero 1"))
    numero_2 = int(input("inresa numero 2"))
    return numero_1 , numero_2

print("bienvenido a tu caculadora digital ")

while True:

        print("1 sumar")
        print("2 restar")
        print("3 dividir")
        print("4 mutiplicar")
        print("5 salir")

ocion = int(input("inresa una ocion"))

if ocion == 1:
        numero_1 , numero_2 = solisitar_dos_numeros()
        print(sumar(numero_1 , numero_2))
elif ocion == 2:
        numero_1 , numero_2 = solisitar_dos_numeros()
        print(restar(numero_1 , numero_2))
elif ocion == 3:
        numero_1 , numero_2 = solisitar_dos_numeros()
        print( division (numero_1 , numero_2))
elif ocion == 4:
        numero_1 , numero_2 = solisitar_dos_numeros()
        print(multiplicar(numero_1 , numero_2))
else:
        print("ocion invalida")
        break


#tomar el ejecicio 1 o el 2 de la prueve
# y tranformalo a programacion funcional
