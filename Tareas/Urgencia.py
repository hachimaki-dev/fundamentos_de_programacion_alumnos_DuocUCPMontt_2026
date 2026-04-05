print("Bienvenido a Urgencias de PYTHON, para continuar necesito que me responda las siguientes preguntas")

edad_del_paciente = int(input("¿Me podria brindad su edad?"))
dificultad_respiratoria = input("Tiene dificultad para respirar (Responder con 'SI' o 'NO')")
nivel_de_dolor = int(input("En una escala del 1 al 10 siendo 1 lo menor y 10 lo mayor. ¿Qué tanto dolor siente?"))

if dificultad_respiratoria == "SI":
    print("Como usted tiene dificultad respiratoria sera atendido de inmediato...")
    print("Espero disfrute de esta Sala de Urgencias de Python")
    import sys
    sys.exit ()
elif dificultad_respiratoria == "NO" and edad_del_paciente > 60:
    print("Como no tiene dificultad respiratoria no es de 'Alta Prioridad', por favor espere")
    print("Le deseamos una bonita estadia en la Sala de Urgencias de Python")
elif nivel_de_dolor < 4:
    print("Lastimosamente tu caso no es del nivel para ser atendido en Urgencias")
    print("Le recomendamos reposo y que vaya a un consultorio, espero tenga buen dia :)")
else:
    print("Por favor espere...")
    print("Esperamos que pueda ser atendido pronto :)")
    