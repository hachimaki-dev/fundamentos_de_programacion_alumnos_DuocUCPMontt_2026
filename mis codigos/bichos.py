

ColeccionGeneral = []
TipoDeBicho = {
    "especie"     #str
    "tamaño"       #int
    "peligrosidad"             #fload
    "peligoso"                 #bool
}
while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Agregar bicho")
        print("2. Buscar bicho")
        print("3. Eliminar bicho")
        print("4. Actualizar estados")
        print("5. Mostrar bichos")
        print("6. Salir")
        print("=====================================")

        opcion_elegida = int(input("que opcion queieres elegir?: "))
        
        if opcion_elegida == 1:
             NonmbreDeBicho = input("escribe el nombre del bicho: ")
             TamañoDelBicho = int(input("de que tamaño es el bicho: "))
             PeligroDelBichoEnNumero = float(input("que nivel de peligrosidad es?: "))
             PeligroDelBichoEscrita = input("¿Es considerado un bicho peligroso? ¿por que?")

             if len (NonmbreDeBicho) > 0 and " " not in NonmbreDeBicho:
                   if NonmbreDeBicho < 0 or " ":
                       print("no puede tener espacios en blanco ni estas vacio")
             
             
            
        










        elif opcion_elegida == 6:
         print("saliendo....")
         break
