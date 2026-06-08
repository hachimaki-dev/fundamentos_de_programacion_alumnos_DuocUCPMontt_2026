# Ejercicio — Sistema de registro de socios en un gimnasio

# 1. Preguntar cuántos socios se registrarán (entero positivo, validado)

# 2. Para cada socio:
# - RUT del socio: mínimo 6 caracteres, sin espacios
# - Edad: entero entre 14 y 80 (validado)

# 3. Clasificar:
# - Menor de 18 → Socio juvenil
# - De 18 a 60   → Socio adulto
# - Mayor de 60  → Socio senior

# 4. Al finalizar mostrar:
# - Cuántos socios de cada categoría
# - Lista de RUTs registrados
categoria_socios_club = {
    "socio_juvenil": 0,
    "socio_adulto" : 0,
    "socio_senior" : 0
}
rut_de_socios = []

while True:
    try:
        cantidad_socios_club = int(input("Ingrese la cantidad de socios"))
        if cantidad_socios_club <= 0:
            print("Socios no pueden ser 0 o numeros negativos")
            continue
        for socios in range(cantidad_socios_club):
            rut_de_cada_socio = str(input("Ingrese el rut del socio"))
            if len(rut_de_cada_socio) < 6 or " " in rut_de_cada_socio or "-" not in rut_de_cada_socio:
                print("Rut debe tener mas de 6 digitos,sin espacios y con guion")
                continue
            rut_de_socios.append(rut_de_cada_socio)
            edad_del_socio = int(input("Ingrese la edad del socio del club :"))
            if edad_del_socio < 14 or edad_del_socio > 80:
                print("Edad invalida debe ser entre 14 y 80 años")
                continue
            if edad_del_socio < 18:
                print("Socio juvenil")
                categoria_socios_club["socio_juvenil"] += 1
            elif edad_del_socio >= 18 and edad_del_socio <= 60:
                print("Socio adulto")
                categoria_socios_club["socio_adulto"] += 1
            elif edad_del_socio > 60:
                print("Socio senior")
                categoria_socios_club["socio_senior"] += 1
        print(f"Socios por categorias \n {categoria_socios_club}")
        print(f"Rut de cada integrante : {rut_de_socios}")
        break
    except Exception as error:
        print(f"Error : {error}")