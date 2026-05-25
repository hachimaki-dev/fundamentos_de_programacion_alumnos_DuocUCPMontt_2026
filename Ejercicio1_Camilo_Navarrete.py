#Desarrollar un programa que permita calcular los valores finales del pack de medicamentos
#para el cuidado de piel y su valor de envio em ña comuna
#Ademas deberas aplicar descuentos segun la edad y tramos

medicamentos=60000
envio=8000
total=0
#tramos=["A", "B", "C", "D"]

edad=int(input("\nPorfavor ingrese su edad \n"))
tramo=input("¿A que tramo pertenece? A B C D\n")

if edad<=30 and (tramo=="A" or tramo=="B"):
    medicamentos=medicamentos*0.82     #PUEDE SER SIMPLEMENTE medicamentos*=0.82 Y SE AHORRA UN POCO DE CODIGO
    total=total+medicamentos+envio
    print(f"Elegiste tramo el tramo {tramo} con eso tu precio en medicamentos ahora sera de\nMedicamentos {medicamentos}")
    print(f"Envio {envio}")
    print(f"Total {total}")
elif edad<=30 and (tramo=="C" or tramo=="D"):
    medicamentos=medicamentos*0.88
    total=total+medicamentos+envio
    print(f"Elegiste tramo el tramo {tramo} con eso tu precio en medicamentos ahora sera de\nMedicamentos {medicamentos}")
    print(f"Envio {envio}")
    print(f"Total {total}")
elif edad>=31 and (edad<=60 and tramo=="A" or tramo=="B"):
    medicamentos=medicamentos*0.88
    total=total+medicamentos+envio
    print(f"Elegiste tramo el tramo {tramo} con eso tu precio en medicamentos ahora sera de\nMedicamentos {medicamentos}")
    print(f"Envio {envio}")
    print(f"Total {total}")
elif edad>=31 and edad<=60 and (tramo=="C" or tramo=="D"):
    medicamentos=medicamentos*0.92
    total=total+medicamentos+envio
    print(f"Elegiste tramo el tramo {tramo} con eso tu precio en medicamentos ahora sera de\nMedicamentos {medicamentos}")
    print(f"Envio {envio}")
    print(f"Total {total}")

elif (tramo=="A" or tramo=="B") and edad>=55:
    envio=envio*0.85
    print(medicamentos)
#NO PUDEEEEEEEEEE WAAAAAAAAAAA

#print(medicamentos)