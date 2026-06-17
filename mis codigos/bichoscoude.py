# ============================================================
#  CAZABICHOS  –  Sistema de registro de bichos capturados
# ============================================================


# ─────────────────────────────────────────────
#  FUNCIONES DE VALIDACIÓN
# ─────────────────────────────────────────────

def validar_especie(especie: str) -> bool:
    """Retorna True si la especie no está vacía ni es solo espacios."""
    return isinstance(especie, str) and especie.strip() != ""


def validar_tamaño(valor: str) -> bool:
    """Retorna True si el valor representa un entero mayor que cero."""
    try:
        return int(valor) > 0
    except ValueError:
        return False


def validar_peligrosidad(valor: str) -> bool:
    """Retorna True si el valor es un float entre 1.0 y 10.0 (inclusive)."""
    try:
        f = float(valor)
        return 1.0 <= f <= 10.0
    except ValueError:
        return False


# ─────────────────────────────────────────────
#  MENÚ
# ─────────────────────────────────────────────

def mostrar_menu() -> None:
    """Imprime las opciones del menú principal."""
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar bicho")
    print("2. Buscar bicho")
    print("3. Eliminar bicho")
    print("4. Actualizar estados")
    print("5. Mostrar bichos")
    print("6. Salir")
    print("=====================================")


def leer_opcion() -> int:
    """Lee y retorna la opción numérica elegida por el usuario (1-6)."""
    while True:
        entrada = input("Elige una opción: ").strip()
        if entrada in {"1", "2", "3", "4", "5", "6"}:
            return int(entrada)
        print("⚠  Opción inválida. Ingresa un número del 1 al 6.")


# ─────────────────────────────────────────────
#  OPERACIONES PRINCIPALES
# ─────────────────────────────────────────────

def agregar_bicho(bichos: list) -> None:
    """Solicita los datos de un bicho, los valida y lo agrega a la lista."""
    print("\n--- Agregar bicho ---")

    especie = input("Especie: ")
    if not validar_especie(especie):
        print("❌ Error: la especie no puede estar vacía ni ser solo espacios.")
        return

    tamaño_str = input("Tamaño (cm, entero > 0): ")
    if not validar_tamaño(tamaño_str):
        print("❌ Error: el tamaño debe ser un número entero mayor que cero.")
        return

    peligrosidad_str = input("Peligrosidad (1.0 – 10.0): ")
    if not validar_peligrosidad(peligrosidad_str):
        print("❌ Error: la peligrosidad debe ser un decimal entre 1.0 y 10.0.")
        return

    bicho = {
        "especie": especie.strip(),
        "tamaño": int(tamaño_str),
        "peligrosidad": float(peligrosidad_str),
        "peligroso": False,        # se calcula al actualizar estados
    }
    bichos.append(bicho)
    print(f"✅ Bicho '{bicho['especie']}' registrado correctamente.")


def buscar_bicho(bichos: list, especie: str) -> int:
    """
    Busca en la lista un bicho cuya especie coincida exactamente con el
    parámetro recibido.
    Retorna la posición (índice) si lo encuentra, o -1 si no existe.
    """
    for i, bicho in enumerate(bichos):
        if bicho["especie"] == especie:
            return i
    return -1


def eliminar_bicho(bichos: list) -> None:
    """Solicita una especie y elimina el bicho correspondiente si existe."""
    print("\n--- Eliminar bicho ---")
    especie = input("Especie del bicho a eliminar: ").strip()

    posicion = buscar_bicho(bichos, especie)
    if posicion == -1:
        print(f"⚠  El bicho '{especie}' no se encuentra registrado.")
    else:
        bichos.pop(posicion)
        print(f"✅ Bicho '{especie}' eliminado correctamente.")


def actualizar_estados(bichos: list) -> None:
    """
    Recorre la lista completa y actualiza el campo 'peligroso' de cada bicho:
    True si su peligrosidad >= 7.0, False en caso contrario.
    """
    for bicho in bichos:
        bicho["peligroso"] = bicho["peligrosidad"] >= 7.0


def mostrar_bichos(bichos: list) -> None:
    """Actualiza estados y muestra todos los bichos registrados."""
    actualizar_estados(bichos)

    print("\n=== LISTA DE BICHOS ===")
    if not bichos:
        print("(No hay bichos registrados aún)")
        return

    for bicho in bichos:
        estado = "PELIGROSO" if bicho["peligroso"] else "NO PELIGROSO"
        print()
        print(f"Especie: {bicho['especie']}")
        print(f"Tamaño: {bicho['tamaño']}")
        print(f"Peligrosidad: {bicho['peligrosidad']}")
        print(f"Estado: {estado}")
        print("*" * 45)


# ─────────────────────────────────────────────
#  PROGRAMA PRINCIPAL
# ─────────────────────────────────────────────

def main() -> None:
    bichos: list = []          # colección global de bichos

    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            agregar_bicho(bichos)

        elif opcion == 2:
            print("\n--- Buscar bicho ---")
            especie = input("Especie a buscar: ").strip()
            pos = buscar_bicho(bichos, especie)
            if pos == -1:
                print(f"⚠  No se encontró ningún bicho con la especie '{especie}'.")
            else:
                bicho = bichos[pos]
                estado = "PELIGROSO" if bicho["peligroso"] else "NO PELIGROSO"
                print(f"\nBicho encontrado en la posición {pos}:")
                print(f"  Especie:      {bicho['especie']}")
                print(f"  Tamaño:       {bicho['tamaño']} cm")
                print(f"  Peligrosidad: {bicho['peligrosidad']}")
                print(f"  Estado:       {estado}")

        elif opcion == 3:
            eliminar_bicho(bichos)

        elif opcion == 4:
            actualizar_estados(bichos)
            print("✅ Estados actualizados correctamente.")

        elif opcion == 5:
            mostrar_bichos(bichos)

        elif opcion == 6:
            print("\nGracias por usar el Cazabichos. ¡Hasta la próxima expedición!")
            break


if __name__ == "__main__":
    main()