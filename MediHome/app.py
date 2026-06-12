import tkinter as tk
from tkinter import ttk, messagebox

medicamentos = []

def limpiar():
    for widget in ventana.winfo_children():
        widget.destroy()

def mostrar_inicio():
    limpiar()

    contenedor = tk.Frame(ventana, bg="#F4F9F9")
    contenedor.pack(expand=True)

    tk.Label(
        contenedor,
        text="MediHome",
        font=("Arial", 34, "bold"),
        bg="#F4F9F9",
        fg="#1B4965"
    ).pack(pady=10)

    tk.Label(
        contenedor,
        text="Recordatorio médico para pacientes con cuidados en el hogar",
        font=("Arial", 15),
        bg="#F4F9F9",
        fg="#555555"
    ).pack(pady=10)

    tk.Button(
        contenedor,
        text="Iniciar",
        font=("Arial", 15, "bold"),
        bg="#1B4965",
        fg="white",
        width=18,
        height=2,
        command=mostrar_app
    ).pack(pady=35)

def mostrar_app():
    limpiar()

    ventana.configure(bg="#F4F9F9")

    tk.Label(
        ventana,
        text="Registro de Medicamentos",
        font=("Arial", 26, "bold"),
        bg="#F4F9F9",
        fg="#1B4965"
    ).pack(pady=25)

    tarjeta = tk.Frame(ventana, bg="white", padx=35, pady=25)
    tarjeta.pack(pady=10)

    tk.Label(tarjeta, text="Medicamento", bg="white", fg="#333333", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w")
    entrada_medicamento = tk.Entry(tarjeta, width=35, font=("Arial", 13))
    entrada_medicamento.grid(row=1, column=0, pady=8)

    tk.Label(tarjeta, text="Dosis", bg="white", fg="#333333", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w")
    entrada_dosis = tk.Entry(tarjeta, width=35, font=("Arial", 13))
    entrada_dosis.grid(row=3, column=0, pady=8)

    tk.Label(tarjeta, text="Hora", bg="white", fg="#333333", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky="w")

    horas = [f"{h:02d}:{m:02d}" for h in range(24) for m in (0, 15, 30, 45)]
    combo_hora = ttk.Combobox(tarjeta, values=horas, width=32, font=("Arial", 12), state="readonly")
    combo_hora.grid(row=5, column=0, pady=8)
    combo_hora.set("Selecciona una hora")

    lista = tk.Listbox(
        ventana,
        width=65,
        height=8,
        font=("Arial", 13),
        bg="white",
        fg="#222222",
        selectbackground="#1B4965"
    )
    lista.pack(pady=20)

    def guardar():
        medicamento = entrada_medicamento.get()
        dosis = entrada_dosis.get()
        hora = combo_hora.get()

        if medicamento == "" or dosis == "" or hora == "Selecciona una hora":
            messagebox.showwarning("Faltan datos", "Completa todos los campos.")
            return

        registro = f"💊 {medicamento}   |   {dosis}   |   {hora}"
        medicamentos.append(registro)
        lista.insert(tk.END, registro)

        entrada_medicamento.delete(0, tk.END)
        entrada_dosis.delete(0, tk.END)
        combo_hora.set("Selecciona una hora")

    botones = tk.Frame(ventana, bg="#F4F9F9")
    botones.pack(pady=10)

    tk.Button(
        botones,
        text="Guardar medicamento",
        font=("Arial", 13, "bold"),
        bg="#2A9D8F",
        fg="white",
        width=22,
        height=2,
        command=guardar
    ).grid(row=0, column=0, padx=10)

    tk.Button(
        botones,
        text="Volver al inicio",
        font=("Arial", 13),
        bg="#D9E2E2",
        fg="#333333",
        width=18,
        height=2,
        command=mostrar_inicio
    ).grid(row=0, column=1, padx=10)

ventana = tk.Tk()
ventana.title("MediHome")
ventana.geometry("850x650")
ventana.configure(bg="#F4F9F9")

mostrar_inicio()
ventana.mainloop()