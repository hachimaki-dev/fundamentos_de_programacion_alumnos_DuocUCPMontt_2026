# Un banco recibe solicitudes de crédito. El analista ingresa el score crediticio de cada solicitante (entero de 0 a 1000).

# Clasifica el score con estos rangos exactos:

# Mayor a 750 (> 750) → "Aprobado automáticamente"
#De 500 a 750 (>= 500 y <= 750) → "Revisión manual"
# Menor a 500 (< 500) → "Rechazado"
# Condiciones de borde: Un score de exactamente 750 es "Revisión manual". Un score de exactamente 500 también es "Revisión manual".

# Registra 8 solicitudes y muestra al final cuántas quedaron en cada categoría.

# Desafío: valida que el score esté entre 0 y 1000. Si no, pide ingresar de nuevo.#
clientes_de_banco = {
    "Aprobados" : 0,
    "Revision manual" : 0,
    "Rechazados" : 0
}
contador_de_solicitudes = 0
while contador_de_solicitudes < 8:
    try:
        puntaje_de_credito = int(input("Ingrese su puntaje acrediticio \n"))
        if puntaje_de_credito < 0 or puntaje_de_credito > 1000:
            print("Puntaje inválido")
            continue
        if puntaje_de_credito > 750:
            print("Aprobado automaticamente")
            clientes_de_banco["Aprobados"] += 1 
        elif puntaje_de_credito >= 500 and puntaje_de_credito <= 750:
            print("Revision manual")
            clientes_de_banco["Revision manual"] += 1 
        elif puntaje_de_credito < 500:
            print("Rechazado")
            clientes_de_banco["Rechazados"] += 1 
        contador_de_solicitudes += 1
    except Exception as error_de_lectura :
        print(f"Se ha producido un error de lectura : {error_de_lectura}")
print(f"Se ha realizado {contador_de_solicitudes} solicitudes de creditos")
print(clientes_de_banco)