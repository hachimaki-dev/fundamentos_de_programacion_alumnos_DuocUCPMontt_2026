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
    print(f"{reset}\n======================\n{negrita}BIENVENIDO A CRUZ AZUL{reset}\n======================")
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
