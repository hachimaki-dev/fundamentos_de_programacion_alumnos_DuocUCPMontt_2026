print("********* Ranking de Superhéroes **********")

misiones_exitosas = int(input("¿Cuantas misiones exitosas a tenido Usted? "))

costo_civil = int(input("¿Cuantos daños civiles(en costo monetario) a tenido en el mes? "))

if misiones_exitosas >= 10 and costo_civil == 0 :
    print("H é r o e   C a t e g o r í a   S.   B o n o   m á x i m o ! ")
elif 5 <= misiones_exitosas <= 9 :
    print("H é r o e   C a t e g o r í a   A.   C u m p l e   p r o m e d i o")
elif misiones_exitosas < 5 and costo_civil > 10000000 :
    print("D e s p e d i d o .  D e m a s i a d o  c a o s ")
else:
    print("H é r o e   e n   o b s e r v a c i ó n")

