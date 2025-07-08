import tkinter as tk
from tkinter import messagebox
import string
import random

# Function to generate password
def generate_password():
    length = password_length.get()
    use_upper = check_upper.get()
    use_lower = check_lower.get()
    use_number = check_number.get()
    use_symbol = check_symbol.get()
    no_repeat = check_unique.get()

    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_number:
        characters += string.digits
    if use_symbol:
        characters += string.punctuation

    if not characters:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, "Please select at least one option")
        return

    if no_repeat and length > len(set(characters)):
        password_entry.delete(0, tk.END)
        password_entry.insert(0, "Too long for unique characters")
        return

    if no_repeat:
        password = ''.join(random.sample(characters, length))
    else:
        password = ''.join(random.choices(characters, k=length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy password
def copy_password():
    pwd = password_entry.get()
    if pwd:
        win.clipboard_clear()
        win.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create GUI window
win = tk.Tk()
win.title("Password Generator")
win.geometry("400x420")
win.config(bg="#a7d3f2")

# Title
tk.Label(win, text="🔐 Generate a Strong Password", font=("Arial", 14, "bold"), bg="#a7d3f2").pack(pady=10)

# Password box
password_entry = tk.Entry(win, font=("Arial", 12), width=30, justify="center")
password_entry.pack(pady=8)

# Copy button
tk.Button(win, text="📋 Copy to Clipboard", command=copy_password, bg="#007acc", fg="white", font=("Arial", 10, "bold")).pack(pady=4)

# Slider for length
password_length = tk.IntVar(value=20)
tk.Scale(win, from_=8, to=32, variable=password_length, orient="horizontal", label="Password Length", bg="#a7d3f2").pack(pady=10)

# Checkboxes
check_upper = tk.BooleanVar(value=True)
check_lower = tk.BooleanVar(value=True)
check_number = tk.BooleanVar(value=True)
check_symbol = tk.BooleanVar(value=True)
check_unique = tk.BooleanVar(value=True)

tk.Checkbutton(win, text="Include Uppercase Letters (A-Z)", variable=check_upper, bg="#a7d3f2").pack(anchor="w", padx=60)
tk.Checkbutton(win, text="Include Lowercase Letters (a-z)", variable=check_lower, bg="#a7d3f2").pack(anchor="w", padx=60)
tk.Checkbutton(win, text="Include Numbers (0-9)", variable=check_number, bg="#a7d3f2").pack(anchor="w", padx=60)
tk.Checkbutton(win, text="Include Symbols (!@#$)", variable=check_symbol, bg="#a7d3f2").pack(anchor="w", padx=60)
tk.Checkbutton(win, text="Avoid Repeating Characters", variable=check_unique, bg="#a7d3f2").pack(anchor="w", padx=60)

# Generate button
tk.Button(win, text="🔁 Generate Password", command=generate_password, bg="#0099cc", fg="white", font=("Arial", 12, "bold")).pack(pady=20)

# Run GUI
win.mainloop()
