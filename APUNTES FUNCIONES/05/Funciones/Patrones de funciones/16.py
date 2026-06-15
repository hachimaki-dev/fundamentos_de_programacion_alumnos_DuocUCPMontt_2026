def contar_aprobados_v2(lista):
    return sum(
        1 for est in lista
        if est["aprobado"]
    )