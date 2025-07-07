import tkinter as tk
import math

# Main Application Window
app = tk.Tk()
app.title("Codesoft Scientific Calculator")
app.geometry("420x580")
app.config(bg="#222831")

current_input = ""
history_list = []

# Display field
def update_input(value):
    global current_input
    current_input += str(value)
    input_var.set(current_input)

def clear_input():
    global current_input
    current_input = ""
    input_var.set("")

def delete_last():
    global current_input
    current_input = current_input[:-1]
    input_var.set(current_input)

def evaluate_expression():
    global current_input
    try:
        result = str(eval(current_input))
        history_list.append(f"{current_input} = {result}")
        input_var.set(result)
        current_input = result
        refresh_history()
    except:
        input_var.set("Error")
        current_input = ""

def apply_scientific(op):
    global current_input
    try:
        val = float(eval(current_input))
        result = None
        if op == "sqrt":
            result = math.sqrt(val)
        elif op == "square":
            result = val**2
        elif op == "log":
            result = math.log10(val)
        elif op == "sin":
            result = math.sin(math.radians(val))
        elif op == "cos":
            result = math.cos(math.radians(val))
        elif op == "tan":
            result = math.tan(math.radians(val))
        input_var.set(str(result))
        current_input = str(result)
        history_list.append(f"{op}({val}) = {result}")
        refresh_history()
    except:
        input_var.set("Math Error")
        current_input = ""

# Update history panel
def refresh_history():
    history_box.delete(0, tk.END)
    for h in history_list[-5:][::-1]:
        history_box.insert(tk.END, h)

# Entry field
input_var = tk.StringVar()
display = tk.Entry(app, textvariable=input_var, font=('Calibri', 24), bg="#393E46", fg="white", bd=0, relief='flat', justify='right')
display.pack(pady=10, padx=10, ipady=15, fill='x')

# Buttons area
btns_frame = tk.Frame(app, bg="#222831")
btns_frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C', '←', 'x²', '√'],
    ['sin', 'cos', 'tan', 'log']
]

for row in buttons:
    row_frame = tk.Frame(btns_frame, bg="#222831")
    row_frame.pack(fill='x', pady=3)
    for btn in row:
        action = lambda x=btn: (
            clear_input() if x == 'C' else
            delete_last() if x == '←' else
            evaluate_expression() if x == '=' else
            apply_scientific('square') if x == 'x²' else
            apply_scientific('sqrt') if x == '√' else
            apply_scientific(x) if x in ['sin', 'cos', 'tan', 'log'] else
            update_input(x)
        )
        tk.Button(row_frame, text=btn, width=8, height=2, font=('Calibri', 14),
                  bg="#00ADB5", fg="white", bd=0, command=action).pack(side='left', padx=5)

# History label
tk.Label(app, text="🕒 History", font=('Calibri', 14), bg="#222831", fg="#EEEEEE").pack(pady=5)
history_box = tk.Listbox(app, height=5, font=('Calibri', 12), bg="#393E46", fg="white")
history_box.pack(fill='both', padx=10, pady=5)

# Run app
app.mainloop()
