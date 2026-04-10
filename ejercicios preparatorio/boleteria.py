import time
import os

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

rojo = '\033[31m'
amarillo = '\033[33m'
negrita = '\033[1m'
gris = '\033[90m'
verde = '\033[32m'
cian = '\033[36m'
reset = '\033[0m'

precio_ptoVaras = 3000
precio_osorno = 7000
precio_frutillar = 5000
atendiendo = True

def opcion_numero(mensaje):
    while True:
        dato = input(mensaje)
        try:
            return int(dato)
        except ValueError:
            print("Por favor elija una opcion valida.")

def opcion_siNo(mensaje):
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta == "si":
            return True
        elif respuesta == "no":
            return False
        else:
            print(f"{rojo}Por favor elige una opción válida (si/no).{reset}")

    
while atendiendo:
    limpiar()
    print(f"\n======================\n{negrita}BIENVENIDO A CRUZ AZUL{reset}\n======================")
    time.sleep(1)
    print("DESTINOS: ")
    print(f"-   {cian}1{reset}. Puerto Varas   {verde}${precio_ptoVaras}{reset}")
    print(f"-   {cian}2{reset}. Osorno         {verde}${precio_osorno}{reset}")
    print(f"-   {cian}3{reset}. Frutillar      {verde}${precio_frutillar}{reset}")
    print(f"\n-   {gris}4. Salir{reset}")

    while True:
        opcion_destino = opcion_numero(f"Por favor ingrese la opcion de su destino:{gris} ")
        print("---")
        if opcion_destino == 4:
            print(f"{reset}Gracias por preferir Cruz Azul")
            atendiendo = False
            break
        if opcion_destino in [1,2,3]:
            break
        else:
            print(f"'{rojo}{negrita}{opcion_destino}{reset}' no es una opcion valida. Por favor intente nuevamente")
    if not atendiendo: break

    if opcion_destino == 1:
        destino_elegido = "Puerto Varas"
        precio_destino = precio_ptoVaras
    elif opcion_destino == 2:
        destino_elegido = "Osorno"
        precio_destino = precio_osorno
    else:
        destino_elegido = "Frutillar"
        precio_destino = precio_frutillar
        
    print(f"{reset}-   Destino seleccionado: {verde}{negrita}{destino_elegido}{reset}")
    
    while True:
        print(f"{reset}Elija el tipo de viaje: \n-   {cian}1{reset}. Solo ida {verde}${precio_destino}{reset}\n-   {cian}2{reset}. Ida y vuelta {verde}${precio_destino * 2}{reset}")
        opcion_viaje = opcion_numero(f"Ingrese la opcion de su viaje:{gris} ")

        if opcion_viaje in [1, 2]:
            break
        print(f"{rojo}Por favor ingrese una opcion valida.{reset}")

    if opcion_viaje == 1:
        while True:
            numero_boletos = opcion_numero(f"{reset}Ingrese la cantidad de asientos a comprar:{gris} ")
            if numero_boletos > 0: break
            print(f"{rojo}Debe comprar al menos 1 asiento")
        subtotal = precio_destino * numero_boletos
    elif opcion_viaje == 2:
        while True:
            numero_boletos = opcion_numero(f"{reset}Ingrese la cantidad de asientos a comprar:{gris} ")
            if numero_boletos > 0: break
            print(f"{rojo}Debe comprar al menos 1 asiento")
        subtotal = (precio_destino * 2) * numero_boletos
    
    print(f"{reset}\n{amarillo}--- RESUMEN DE COMPRA ---{reset}")
    if subtotal > 10000:
        precio_total = subtotal * 0.9
        descuento = subtotal - precio_total
        print(f"SUBTOTAL: {verde}${subtotal}{reset}")
        print(f"DESCUENTO DEL {amarillo}10%{reset}: {verde}{descuento}{reset}")
        print(f"TOTAL A PAGAR: {verde}${precio_total}{reset}")
    else:
        precio_total = subtotal
        print(f"TOTAL A PAGAR {gris}(NO APLICAN DESCUENTOS){reset}: {verde}${precio_total}{reset}")
    
    if not opcion_siNo(f"\n{gris}¿Desea atender a un nuevo cliente? (si/no): "):
        print(f"{reset}Cerrando sistema. \n{negrita}{verde}¡Gracias por preferir Cruz Azul!{reset}")
        atendiendo = False

























'''precio_final = 0
precio_boletos = 0
destino_1 = 1
destino_2 = 2
destino_3 = 3
confirmar_compra = False

cantidad_boletos = None
boleto_ida = 1
boleto_ida_vuelta = 2

print("BIENVENIDO A CRUZ AZUL")
print("====================")
print("ELIJA SU DESTINO:")
print(f"-     1. Puerto Varas ${precio_PV} ")
print(f"-     2. Osorno ${precio_osorno} ")
print(f"-     3. Frutillar ${precio_frutillar} ")

opcion_destino = int(input("Por favor ingrese la opcion de su destino: "))

while True:
    if opcion_destino == 1:
        print(f"Su destino es Puerto Varas.\nSeleccione el tipo de viaje:\n -     1. Solo ida ${precio_PV}.\n -     2. Ida y vuelta ${precio_PV * 2}.")
        opcion_viaje = int(input("Ingrese la opcion de su viaje: "))
        if opcion_viaje == 1:
            print("Cuantos asientos desea comprar?")
            cantidad_boletos = int(input("Ingrese la cantidad de asientos a comprar: "))
            if cantidad_boletos > 0:
                precio_boletos = precio_PV * cantidad_boletos
                if precio_boletos > 10000:
                    precio_final = precio_boletos * 0.9
                    precio_descuento = precio_boletos - precio_final
                    print(f"SUBTOTAL: {precio_boletos}")
                    print(f"DESCUENTO: {precio_descuento}")
                    print(f"TOTAL: {precio_final}")
                    pagar = int(input("1. Para terminar"))
                elif cantidad_boletos == 0:
                    print("volviendo al menu")
                else:
                    precio_final = precio_boletos
                    print(f"SUBTOTAL: {precio_final}")
            elif cantidad_boletos <= 0:
                print("regresando al menu")
        elif opcion_viaje == 2:
            print("Cuantos asientos desea comprar?")
            cantidad_boletos = int(input("Ingrese la cantidad de asientos a comprar: "))
            if cantidad_boletos > 0:
                precio_boletos = precio_PV * cantidad_boletos
                if precio_boletos > 10000:
                    precio_final = precio_boletos * 0.9
                    precio_descuento = precio_boletos - precio_final
                    print(f"SUBTOTAL: {precio_boletos}")
                    print(f"DESCUENTO: {precio_descuento}")
                    print(f"TOTAL: {precio_final}")
                elif cantidad_boletos == 0:
                    print("volviendo al menu")
                else:
                    precio_final = precio_boletos
                    print(f"TOTAL: {precio_final}")


while True:
    try:
        
    except ValueError:
        print("POR FAVOR INGRESE UNA OPCION VALIDA")'''