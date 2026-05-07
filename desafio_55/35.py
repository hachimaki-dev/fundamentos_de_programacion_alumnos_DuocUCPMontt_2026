#Eres auditor del banco y necesitas separar las transferencias sospechosas.

#Datos Iniciales: Las transferencias del día fueron `[15000, 80000, 2000, 150000]`.

#Reglas de Negocio: Cualquier transferencia que sea mayor a 50000 pesos es considerada 'Alto Perfil' y debe ser separada en una lista especial para ser investigada. Las más chicas se ignoran.

#Restricciones: Crea una lista en blanco llamada `importantes`. Usa un `for` para recorrer las transferencias y, con un `if`, mete usando `.append()` solo las que cumplan la regla a tu nueva lista. Imprime la nueva lista.
transferencia_del_dia = [15000, 80000,2000,150000]
importantes = []
for monto in transferencia_del_dia:
    if monto > 50000:
        importantes.append(monto)
print(importantes)

