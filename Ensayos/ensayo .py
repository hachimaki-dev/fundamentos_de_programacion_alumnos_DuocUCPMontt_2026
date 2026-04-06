'''
Se requiere programar el menú de un cajero automático muy rudimentario. Tienes un saldo inicial de $50000. El cajero muestra un menú y operará repetidamente hasta que se elija 'Salir'.

Menú:
1) Ver Saldo
2) Girar Dinero
3) Inversión
4) Salir

El comportamiento debe ser el siguiente:
- Si elige 1: Muestra el saldo actual.
- Si elige 2: Pregunta cuánto girar. A su vez, debes verificar que el monto solicitado sea menor o igual al saldo, y que sea múltiplo de 5000. Si cumple esto, realiza el giro (resta el saldo); si no, muestra el motivo del error ('Saldo insuficiente' o 'Monto no aceptado').
- Si elige 3: Te ofrece invertir tu dinero. Te solicita una cantidad. Si esa cantidad es menor que o igual a tu saldo, te la duplica y la añade al saldo final de retorno, sino, muestra 'Saldo insuficiente'.
- Si elige 4: Termina el programa imprimiendo "Cajero apagado".
- Cualquier otra opción muestra 'Opción inválida'.

Usa while y condicionales anidados (if dentro de if equivalentes) para este desafío
'''

# La indentación es el salto de línea necesario para los if, else, elif, while y for.
'''
if True :
    print("If")
else :
    print("Else")
'''

# {} = Llaves -> Se usa en las variables dentro de los prints o inputs.
# [] = Corchetes -> Se usa en listas.
# () = Paréntesis -> Se usa en funciones.

# print(f" {nombre_variable} ")
print("banco de ensayo")
saldo_total = 0
while True :
    print(f"saldo actual: {saldo_total}")
    print("1. depositar")
    print("2. retirar")
    print("3. salir")

    opcion = int(input(" elije "))
    
    if opcion == 1 : # Esta opción deposita plata
        saldo_depositado = int(input("cuanto saldo desea depositar"))

        saldo_total = saldo_total + saldo_depositado

    if opcion == 2 : # Esta opción retira plata
        saldo_retirado = int(input("saldo a retirar"))
        
        if saldo_total < saldo_retirado:
            print("no Hay saldo suficiente")
        else :
            saldo_total = saldo_total - saldo_retirado

    if opcion == 3 : # Sale del programa (Lo termina)
        break
                             

 