def sumar(numero_1, numero_2):
    return numero_1 + numero_2

def restar(numero_1, numero_2):
    return numero_1 - numero_2

def multiplicar(numero_1, numero_2):
    return numero_1 * numero_2

def dividir(numero_1, numero_2):
    return numero_1 // numero_2

while True :
    operacion_elegida = int(input("Eliga que operación desea realizar en esta oportunidad: 1.Suma    2.Resta    3.Multiplicación    4.División    5.Salir "))
    if operacion_elegida == 1 :
        print("Usted ha elegido sumar")
        primer_numero = int(input("Ahora eliga el primer número de su operación: "))
        segundo_numero = int(input("Ahora eliga el segundo: "))
        print(sumar(primer_numero, segundo_numero))
        break
    elif operacion_elegida == 2 :
        print("Usted ha elegido restar")
        primer_numero = int(input("Ahora eliga el primer número de su operación: "))
        segundo_numero = int(input("Ahora eliga el segundo: "))
        print(restar(primer_numero, segundo_numero))
        break
    elif operacion_elegida == 3 :
        print("Usted ha elegido multiplicar")
        primer_numero = int(input("Ahora eliga el primer número de su operación: "))
        segundo_numero = int(input("Ahora eliga el segundo: "))
        print(multiplicar(primer_numero, segundo_numero))
        break
    elif operacion_elegida == 4 :
        print("Usted ha elegido dividir")
        primer_numero = int(input("Ahora eliga el primer número de su operación: "))
        segundo_numero = int(input("Ahora eliga el segundo: "))
        print(dividir(primer_numero, segundo_numero))
        break
    elif operacion_elegida == 5 :
        print("Usted ha elegido simplemente salir, Adiós")
        break
    else :
        print("Su elección es inválida, recuerde elegir su operación insertando su respectivo número.")