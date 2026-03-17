import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Calculadora")
root.geometry('400x500')
root.resizable(0, 0)

color_texto = "#000000"
color_boton = "#e0e0e0"
color_boton_igual = "#4caf50"
color_boton_clear = "#072323"

screen_text = tk.StringVar()
screen_label = tk.Label(root, textvariable=screen_text, font=("Arial", 30), bg='#ffffff', fg=color_texto, anchor="e", padx=10)
screen_label.grid(row=0, column=0, columnspan=4, sticky="we", pady=10)

expression = ''

def press(num):
    global expression
    expression += str(num)
    screen_text.set(expression)

def equalpress():
    try:
        global expression
        result = str(eval(expression))
        screen_text.set(result)
        expression = result
    except Exception as e:
        messagebox.showerror("Error", "Entrada no valida")
        screen_text.set('')
        expression = ''
    
def clear():
    global expression
    screen_text.set('')
    expression = ''

buttons = {
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('3', 3, 0), ('2', 3, 1), ('1', 3, 2), ('+', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('-', 4, 2)
}

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), bg=color_boton, fg=color_texto,
                       command=lambda t=text: press(t))
    button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

equal_button = tk.Button(root, text='=', width=5, height=2, font=('Arial', 18), bg=color_boton_igual, fg='#ffffff', command=equalpress)
equal_button.grid(row=4, column=3, padx=5, pady=5, sticky='nsew')

clear_button = tk.Button(root, text='C', width=5, height=2, font=('Arial', 18), bg=color_boton_clear, fg='#ffffff', command=clear)
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')

for i in range(5):
    root.grid_rowconfigure(1, weight=1)
for i in range(4):
    root.grid_columnconfigure(1, weight=1)

root.mainloop()