#Ejercicio 1 — Formulario básico de validación
#Contexto: Estás construyendo un formulario de registro básico.
#Lo que debe hacer el programa: Pide la edad. Debe ser un entero positivo 
#(> 0). Si ingresa texto, 0 o negativo, avisa: "Entrada inválida. Ingresa un número entero positivo." 
#y vuelve a preguntar. Si es válido, muestra: "Edad registrada: X años."
def validacion_edad():
    while True:
        try:
            edad_usuario = int(input("ingresa tu edad : "))
            if edad_usuario > 0:
                print(f"Edad registrada: {edad_usuario} años.")
            print("Entrada inválida. Ingresa un número entero positivo.")
        except ValueError :
            print("ingresa un numero valido")


validacion_edad()
