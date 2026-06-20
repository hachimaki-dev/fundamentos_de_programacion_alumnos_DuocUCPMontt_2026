lista_De_todos_los_libros = []

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print(f"1. Agregar libro")
    print(f"2. Buscar libro")
    print(f"3. Eliminar libro")
    print(f"4. Actualizar disponibilidad")
    print(f"5. Mostrar libros")
    print(f"6. Salir")
    print("=====================================")

def OpcionMenuElegida():
    while True:

        opcion_elegida = input("Ingrese su opción (1 al 6)")

        if opcion_elegida in ["1", "2", "3", "4", "5", "6"]:

         return opcion_elegida 

        else:
            print("Opción invalida, vuelva a intentarlo") 
        


def ValidarTitulo():
   while True:
      TituloDelLibro = input("cual es el nombre del libro?: ")
      # ❌ ANTES: if len(TituloDelLibro) <= 0:
      # Problema: si el usuario escribía solo espacios (ej. "   "), len() devolvía 3,
      # y el texto pasaba como válido aunque estuviera vacío en la práctica.
      # ✅ CORRECCIÓN: se agregó .strip() para eliminar espacios antes de medir
      if len(TituloDelLibro.strip()) <= 0:
         print("nombre invalido intente de nuevo")
      else:
         return TituloDelLibro  

def ValidarAutor():
   while True:
      AutorDelLibro = input("cual es el autor del libro?: ")
      # ❌ ANTES: if len(AutorDelLibro) <= 0:
      # Mismo problema que en ValidarTitulo(): no detectaba textos de solo espacios.
      # ✅ CORRECCIÓN: se agregó .strip()
      if len(AutorDelLibro.strip()) <= 0:
         print("nombre invalido intente de nuevo")
      else:
         return AutorDelLibro 
      
def ValidarEjemplares():
    while True:
        try:
            EjemplaresDelLibro = int(input("cuantos ejemplares son?: "))

            if EjemplaresDelLibro < 0:
                print("tiene que ser un numero mayor o igual a 0")
            else:
                return EjemplaresDelLibro

        except ValueError:
            print("error intentelo de nuevo")

def AgregarLibro():
   TituloValido = ValidarTitulo()
   AutorValido = ValidarAutor()
   EjemplaresValidos = ValidarEjemplares()
   
   DatosDelLibro = {
      "titulo" : TituloValido,
      "autor" : AutorValido,
      "ejemplares" : EjemplaresValidos,
      "disponible": False 
      }
   
   lista_De_todos_los_libros.append(DatosDelLibro)

# ❌ ANTES:
# def MostrarTodosLosLibros():
#    print(lista_De_todos_los_libros)
# Problema: imprimía la lista completa "en crudo" (como diccionario de Python),
# sin el formato pedido (Título/Autor/Ejemplares/Estado) ni actualizar disponibilidad antes.
# ✅ CORRECCIÓN: ahora llama a ActualizarDisponibilidad() primero, y recorre
# la lista con un for, imprimiendo cada campo con el formato exacto de la consigna.
def MostrarTodosLosLibros():
   ActualizarDisponibilidad()
   print("=== LISTA DE LIBROS ===")
   print()
   for cada_libro in lista_De_todos_los_libros:
      print(f"Título: {cada_libro['titulo']}")
      print(f"Autor: {cada_libro['autor']}")
      print(f"Ejemplares: {cada_libro['ejemplares']}")
      if cada_libro["disponible"]:
         print("Estado: DISPONIBLE")
      else:
         print("Estado: SIN EJEMPLARES")
      print("*******************************************")

def BuscaLibro(NombreDelLibroABuscar):
   for cada_libro in lista_De_todos_los_libros:
      if cada_libro["titulo"] == NombreDelLibroABuscar:
         print("encontrado")
         indice_del_libro_encontado = lista_De_todos_los_libros.index(cada_libro)
         return indice_del_libro_encontado

# ❌ ANTES:
# def Eliminar_libro_por_nombre(NombreDelLibroABuscar):
#    indice_del_libro_encontado = BuscaLibro(NombreDelLibroABuscar)
#    lista_De_todos_los_libros.pop(indice_del_libro_encontado)
#    return True
# Problema: si el libro no existía, BuscaLibro() retornaba None, y
# lista.pop(None) rompía el programa con un TypeError.
# ✅ CORRECCIÓN: se agregó un if para verificar que el índice no sea None
# antes de intentar eliminar; si no existe, retorna False en vez de fallar.
def Eliminar_libro_por_nombre(NombreDelLibroABuscar):
   indice_del_libro_encontado = BuscaLibro(NombreDelLibroABuscar)
   if indice_del_libro_encontado is not None:
      lista_De_todos_los_libros.pop(indice_del_libro_encontado)
      return True
   else:
      return False

def ActualizarDisponibilidad():
   for cada_libro in lista_De_todos_los_libros:
      if cada_libro["ejemplares"] > 0:
         cada_libro["disponible"] = True
      else:
         cada_libro["disponible"] = False
   

def IniciarPrograma():
   while True:
      mostrar_menu()
      opcion_seleccionada = OpcionMenuElegida()

      if opcion_seleccionada == "1":
         AgregarLibro()

      elif opcion_seleccionada == "2":
         nombre_de_libro_a_buscar = input("como se llama el libro?: ")
         indice_del_libro_encontado = BuscaLibro(nombre_de_libro_a_buscar)
         if indice_del_libro_encontado is not None:
            print("libro encontrado")
            print(f"{lista_De_todos_los_libros[indice_del_libro_encontado]['titulo']}")
            print(f"{lista_De_todos_los_libros[indice_del_libro_encontado]['autor']}")
            print(f"{lista_De_todos_los_libros[indice_del_libro_encontado]['ejemplares']}")
            print(f"{lista_De_todos_los_libros[indice_del_libro_encontado]['disponible']}")
         else:
            print("el libro no existe")

      elif opcion_seleccionada == "3":
         nombre_De_libro_a_eliminar = input("que libro quieres eliminar?: ")
         fue_eliminado = Eliminar_libro_por_nombre(nombre_De_libro_a_eliminar)
         # ❌ ANTES: if fue_eliminado is not None:
         # Problema: ahora Eliminar_libro_por_nombre() retorna True o False (nunca None),
         # así que comparar "is not None" siempre sería verdadero, incluso si fue False.
         # ✅ CORRECCIÓN: se compara el valor booleano directamente
         if fue_eliminado:
            print("libro eliminado")
         else:
          # ❌ ANTES: print("ese libro no existe")
          # ✅ CORRECCIÓN: mensaje exacto pedido por la consigna
          print(f"El libro '{nombre_De_libro_a_eliminar}' no se encuentra registrado.")

      elif opcion_seleccionada == "4":
         ActualizarDisponibilidad()
         print("Disponibilidad actualizada")

      elif opcion_seleccionada =="5":
         # ❌ ANTES: print(lista_De_todos_los_libros)
         # ✅ CORRECCIÓN: ahora usa la función con el formato correcto
         MostrarTodosLosLibros()

      elif opcion_seleccionada == "6":
         # ❌ ANTES: print("saliendo.....")
         # ✅ CORRECCIÓN: mensaje exacto pedido por la consigna
         print("Gracias por usar el sistema. ¡Hasta pronto!")
         break

      # ❌ ANTES: no existía ningún else aquí
      # ✅ CORRECCIÓN: se agregó por consistencia y buena práctica
      else:
         print("La opción ingresada no es una opción válida")


IniciarPrograma()