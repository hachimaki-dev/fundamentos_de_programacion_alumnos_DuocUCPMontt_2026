print ("===============================")
print ("======Triage de Hospital=======")
print ("===============================\n")

import sys 
import time

print ("!Bienvenido a Urgencias¡\n")
print ("Aquí podremos atenderete de manera segura.")
print ("Ten encuenta que te atenderemos en base a tu nivel de gravedad.")
print ("Debido a que contamos con 5 secciónes que nos diran tu estado.\n")
print ("Las cuales son : \n")

print ("1. C1 (Emergencía), 'atención inmediata, aplica en casos de accidentes graves o con riesgo de vida'. ")
print ("2. C2 (Muy urgente), 'Atención rapida, aplica en caso donde la situacón puede empeorar'.  ")
print ("3. C3 (Urgente), 'Atención media, aplica en casos como fracturas o fiebre alta,")
print ("4. C4 (Leve), 'Atención moderada, aplica en casos como resfrios o dolores leves ")
print ("5. C5 (No urgente), 'Atención baja, aplica es situciones donde puede esperar por un periodo largo de tiempo'. \n ")

print ("Dicho esto, por favor ingrese su nombre a continuacón.")
Nombre_Paciente = str(input("Escriba su Nombre : ")).lower()
print (f"Encantado de conocerlo {Nombre_Paciente} ahora Ingrese su edad en la sección de abajo.")
print ("Esto se solicita para catalogarlo en secciónes diferentes, contamos con varias y son las siguientes.\n")
print ("1. A1 (Sala de niños de entre 1 a 13.)")
print ("2. A2 (Sala de jovenes de entre 14 a 25.)")
print ("3. A3 (Sala de adultos de entre 26 50.)")
print ("4. A4 (Sala de adultos mayores de entre 50 a 99).\n")
Edad_de_Paciente = int(input("Ingrese su edad : "))

print ("Muy bien, ahora le comunicamos en que sección debe de ir.\n")
time.sleep(2)



if Edad_de_Paciente >=1 and Edad_de_Paciente <13:
    print 

elif Edad_de_Paciente >=14 and Edad_de_Paciente  <=25 :
    print (f"Estimado {Nombre_Paciente}. Usted debera ir a la sección 2A debido a que su edad es {Edad_de_Paciente}")

elif Edad_de_Paciente >= 26 and Edad_de_Paciente <=50:
    print (f"Estimado {Nombre_Paciente}. Ustede debera ir a la sección 3A debido a que su edad es {Edad_de_Paciente}.")

elif Edad_de_Paciente >=50 and Edad_de_Paciente <=99:
    print (f"Estimado {Nombre_Paciente}. Usted debera ir a la sección 4A debido a que su edad es {Edad_de_Paciente}")
    print ("La sección se encuentra bastante lejos, ¿no quiere que lo ayudemos a llegar?\n")
    Opinion_Paciente = str(input("Confirme si desea ayuda con 'Si' o 'No' : ")).lower()
    if Opinion_Paciente == "si" :
        print ("Enseguida lo ayudamos.\n")
        time.sleep(2)
        print ("Bien, por favor sientese aquí y lo llevaremos a su sección.")
        print ("Esto puede demorar ya que se encuentra lejos.\n")
        time.sleep(5)
        print ("Bien, ya hemos llegado, ahora espere pacientemente a que llegue la enfermera que la atendera.")

        print (f"Bien, {Nombre_Paciente} cuenteme su situación con la escala mencionada anteriormente.")
        print ("Con la escala mencionada anteriormente.\n")
        
        Estado_de_paciente = str(input("Ingrese su estado : "))
        if Estado_de_paciente == "c1":
            print ("!ESTADO DE EMERGENCIA¡\n")  
            print ("Paciente en estado de emergencia")
            print ("Cuenteme más sobre su salud. ¿Tienes problemas para respirar? Confirme 'SI' o 'NO' ")
            respuesta_de_usuario = str(input("Cofirme su respusta : ")).lower()
            if respuesta_de_usuario == "si" :
                print ("¿De cuanto es su dolor?. 1 al 10.\n")
                nivel_de_dolor_de_paciente = int(input("Ingrese su nivel de dolor : "))
                if nivel_de_dolor_de_paciente >=8 and nivel_de_dolor_de_paciente <=10 :
                    print ("LO llevaremos altiro caballero, por ahora trate de mantener la calma.")
                
                elif nivel_de_dolor_de_paciente >=5 and nivel_de_dolor_de_paciente <=7 and Edad_de_Paciente >=50 :
                    print (f"bien, con respecto a su {Edad_de_Paciente} lo llevaremos a urgencias, por ahora trate de mantener la calma")
                
                elif nivel_de_dolor_de_paciente >=3 and nivel_de_dolor_de_paciente <=4:
                    print ("Espere pacientemente, en seguida lo llamaremos o vaya a consultorio.")

                elif nivel_de_dolor_de_paciente >=1 and nivel_de_dolor_de_paciente <=3:
                    print ("vaya a consultorio y espere su respuesta pero aún asi es recomendable que vaya a casa con la receta que le entregaremos.")
        
            elif respuesta_de_usuario == "no" :
                print ("Bueno, entonce de igual manera vamos a monitorearlo.")

                

                  

        




    











    elif Opinion_Paciente == "no":
        print ("¿Esta seguro de su elección?. Escriba 'Si' o 'No' en la sección de abajo.")
        Reafirmacióo_del_paciente = str(input ("Escriba su respuesta : ")).lower()
        if Reafirmacióo_del_paciente == "si":
            print ("Bien, ahora lo llevamos a su sección, espere pacientemente.")
            time.sleep(3)

        elif Reafirmacióo_del_paciente == "no":
            print ("la sección se encuentra ")
    
    








