import time
import sys 

print ("/==========================================/")
print ("/======Vamos a rankear tu Superhéroes======/")
print ("/==========================================/\n")

print ("En este programa vamos a rankear a tú superhéroe.")
print ("Solo debe de ingresar dos cosas mínimas.\n")

print ("1. Misiones Exitosas (Define que Categoria es (S) , (A) y (D)).")
print ("2. Daño Civiles (Define que categoría es (S) , (A) , (D)).")
print ("3. Los daños civiles deben ser ingresado en $(Costo monetario).\n")

print ("Con todo esto mencionado.")
print ("En la sección de abajo, ingrese el nombre de su superhéroe.\n")

nombre_de_superheroe = str(input("¿Nombre del superhéroe? : "))
print ()

print (f"umh, ¿{nombre_de_superheroe}? como quieras.")
print ("Igual me parece buen nombre.")
print ("Ahora vamos a rankear a tu superhéroe.\n")

print ("En la sección de abajo debe de ingresar la cantidad de 'misiones exitosas' de tu superhéroe.\n")

Misiones_exitosas = int(input("¿Cuántas misiones exitosas? : "))
print ()
print (f"UMH, para un superhéroe llamado {nombre_de_superheroe} no esta tan mal.")
print ("Bien, ahora ingrese los daños civiles.")
print ("Recuerde que debe de ser en montos monetarios.\n")

daños_civiles = int(input("¿hay daños civiles? : "))
print()
print ("Bien, igual es bueno, o eso creo.\n")

print (f"Ahora vamos a procesar en que categoria debe de estar {nombre_de_superheroe}. \n")

print ("PROCESANDO...\n")
time.sleep(4)

if Misiones_exitosas > 10 and daños_civiles == 0 :
    print (f"El superhéroe llamado {nombre_de_superheroe}. ES CLASE S.")
    print ("Superhéroe recomendado.")

elif Misiones_exitosas >5 and Misiones_exitosas < 9:
    print (f"El superheroé llamdo {nombre_de_superheroe}. ES CLASE A.")
    print ("Superhéroe promedio.")

elif Misiones_exitosas < 4 :
    print ("El superhéroe ha sido despedido.")

else:
    print ("Superhéroe en observación.")










