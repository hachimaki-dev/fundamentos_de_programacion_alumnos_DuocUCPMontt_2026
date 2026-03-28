#division entera : divide el primer valor por el segundo y devuelve un resultado de tipo entero 
#modulo : deuvelve el resto de la division entre el primer valor y el segundo
#exponenciacion : eleva el primer valor a la potencia del segundo

a= 10 
b = 3 
suma= a + b #13
resta= a + b  #7
multiplicacion= a * b # 30 
division = a/b #3.333333
division_entera = a//b #3
modulo = a%b #1
exponenciacion = a**b #1000

# comparacion 

#igual a (==) : devuelve un verdadero si ambos valores son iguales
#diferente de (!=) : devuelve verdadero si los valores son diferentes
#mayor que (>): devuelve verdadero si el primer valor es mayor que el segundo
#menor que (<) : devuelve verdadero si el primer valor es menor que el segundo
#mayor o igual que (>=) : devuelve verdadero si el primer valor es mayor o igual que el segundo 
#menor o igual que (<=) : devuelve verdadero si el primer valor es menor o igual que el segundo
a = 10 
b = 3

igual = a == b #False
diferente = a != b #True 
mayor_que = a > b #True
menor_que = a < b # False
mayor_o_igual = a >= b #True
menor_o_igual = a <= b #False

#Compuertas Logicas 
#Los operaciones logicos se utilizan para combinar expresiones condicionales y evaluar multiples condiciones.
#AND (and) : devuelve Verdadero si ambas condiciones son verdaderas
#OR (or) : devuelve Verdadero si al menos una de las condiciones es Verdadera
#NOT (not) : invierte el valor de una condicion , devuelve Verdadero si la condicion es falsa y Falsa si la condicion es verdadera , una denegada

a = 10 
b = 3

resultado_and = (a> 5) and (b < 5) # True por que 10 es mayor que 5 y 3 es menor que 5 entonces gana el de mayor numero
resultado_or = (a > 15) or (b < 5) #True por que 3 es menor que 5 entonces la salida es verdadera
resultado_not = not (a > 5) #False

#Ciertos operadores tienen mas prioriedad sobre otros , la precedencia sigue el siguiente orden : parentesis , exponenciacion , multiplicacion/division , suma/resta , operadores de comparacion y operadores logicos